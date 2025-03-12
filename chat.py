from pathlib import Path
import streamlit as st

# Add at top of file
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 1) Configura a página no topo do script (sem parâmetros extras em rerun)
st.set_page_config(
    page_title="CHATSeek - Assistente Virtual",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os
import time
import uuid
import json
import datetime
import re
# Imports da sua aplicação de IA:
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Imports dos módulos de estilo
from assets import base, sidebar, chat, syntax
from assets import sidebar_extra, header, typing

# ========== Funções utilitárias de formatação ==========
def format_links(text):
    url_pattern = r'https?:#//(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.sub(
        url_pattern,
        lambda match: f'<a href="{match.group(0)}" target="_blank" style="color: var(--marca-purple); text-decoration: underline;">{match.group(0)}</a>',
        text
    )

def format_markdown(text):
    """Format markdown text with improved code block handling."""
    # Process code blocks first
    def replace_code_block(match):
        lang = match.group(1) or ''
        code = match.group(2).strip()
        # Não usar re.escape para não interferir na sintaxe do código
        return f'<pre><code class="language-{lang}">{code}</code></pre>'
    
    # Replace code blocks with HTML
    text = re.sub(r'```([\w\+]*)\n?(.*?)```', replace_code_block, text, flags=re.DOTALL)
    
    # Format other markdown elements - corrigido para capturar ambos os grupos
    text = re.sub(r'\*\*(.+?)\*\*|__(.+?)__', lambda m: f'<strong>{m.group(1) or m.group(2)}</strong>', text)
    text = re.sub(r'\*(.+?)\*|_(.+?)_', lambda m: f'<em>{m.group(1) or m.group(2)}</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    
    return text

# ========== Lógica do Chat ==========
class ChatApplication:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            top_p=0,
            streaming=True,
            api_key=os.getenv("API_KEY")
        )
        self.session_histories = {}
        # "chain" que registra histórico de mensagens
        self.chain = RunnableWithMessageHistory(
            self.llm,
            self.get_session_history,
            input_messages_key="messages",
            history_messages_key="history"
        )
        self.title_llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            api_key=os.getenv("API_KEY")
        )

    def get_session_history(self, session_id):
        if session_id not in self.session_histories:
            self.session_histories[session_id] = ChatMessageHistory()
        return self.session_histories[session_id]

    def generate_response(self, message, session_id):
        if isinstance(message, HumanMessage):
            inputs = {"messages": [message]} 
        else:
            inputs = {"messages": [HumanMessage(content=str(message))]}
        
        config = {"configurable": {"session_id": session_id}}
        
        try:
            for chunk in self.chain.stream(inputs, config):
                # Verificar se o usuário cancelou a resposta
                if 'cancel_response' in st.session_state and st.session_state.cancel_response:
                    yield AIMessage(content="Resposta cancelada pelo usuário.")
                    return
                yield chunk
        except Exception as e:
            logger.error(f"Chain error for session {session_id}: {e}")
            try:
                # Fallback to direct LLM
                for chunk in self.llm.stream([message]):
                    # Verificar cancelamento também no fallback
                    if 'cancel_response' in st.session_state and st.session_state.cancel_response:
                        yield AIMessage(content="Resposta cancelada pelo usuário.")
                        return
                    yield chunk
            except Exception as inner_e:
                logger.error(f"LLM fallback error: {inner_e}")
                yield AIMessage(content=f"An error occurred: {str(e)}")

    def generate_conversation_title(self, messages, session_id):
        """Generate a short title for the conversation."""
        if not messages or len(messages) < 2:
            return f"New conversation {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
        
        # Take first few messages for context
        context = messages[:min(4, len(messages))]
        
        prompt = (
            "Create a short descriptive title (max 40 chars) for this conversation:\n\n"
            "Rules:\n"
            "- Be concise but descriptive\n"
            "- Use sentence case\n"
            "- No quotes or special characters\n\n"
            "Messages:\n"
        )
        
        for msg in context:
            role = "User" if isinstance(msg, HumanMessage) else "Assistant"
            content = msg.content[:100] + "..." if len(msg.content) > 100 else msg.content
            prompt += f"{role}: {content}\n"
            
        try:
            response = self.title_llm.invoke([HumanMessage(content=prompt)])
            title = response.content.strip().strip('"').strip("'")
            return title[:40]
        except Exception as e:
            logger.error(f"Title generation error: {e}")
            return f"Conversation {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"

# ========== Interface com Streamlit ==========
class StreamlitInterface:
    def __init__(self):
        self.app = ChatApplication()
        self._init_session_state()
        self._inject_custom_css()

    def _inject_custom_css(self):
        """Injeta todo o CSS modularizado"""
        css = f"""
        <style>
            @import url('https:#//fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
                        
            {base.get_base_css()}
            {sidebar.get_sidebar_css()}
            {sidebar_extra.get_sidebar_extra_css()}
            {chat.get_chat_css()}
            {syntax.get_syntax_css()}
            {header.get_header_css()}
            {typing.get_typing_css()}
        </style>
        """
        
        # Garantir que as variáveis CSS sejam definidas
        st.markdown(css, unsafe_allow_html=True)

    @staticmethod
    def _init_session_state():
        # Inicializa variáveis de estado
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if 'processing' not in st.session_state:
            st.session_state.processing = False
        if 'current_conversation_id' not in st.session_state:
            st.session_state.current_conversation_id = str(uuid.uuid4())
        if 'saved_conversations' not in st.session_state:
            try:
                with open("saved_conversations.json", "r") as f:
                    st.session_state.saved_conversations = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                st.session_state.saved_conversations = {}
            
    def _save_conversations(self):
        with open("saved_conversations.json", "w") as f:
            json.dump(st.session_state.saved_conversations, f)

    def _save_current_conversation(self):
        """Salva a conversa atual no dicionário e no arquivo."""
        if not st.session_state.chat_history:
            return
        
        cid = st.session_state.current_conversation_id
        # Verificar se a conversa já existe
        is_existing = cid in st.session_state.saved_conversations
        
        # Se já existir, mantém o título e o timestamp originais; senão, gera novos
        if is_existing:
            title = st.session_state.saved_conversations[cid].get("title", "")
            # Preservar o timestamp original para manter a ordem no histórico
            timestamp = st.session_state.saved_conversations[cid].get("timestamp", "")
            if not timestamp:  # Se por algum motivo não tiver timestamp, criar um novo
                timestamp = datetime.datetime.now().isoformat()
        else:
            title = self.app.generate_conversation_title(st.session_state.chat_history, cid)
            # Nova conversa recebe timestamp atual
            timestamp = datetime.datetime.now().isoformat()
            
        st.session_state.saved_conversations[cid] = {
            "title": title,
            "messages": [
                {
                    "role": "user" if isinstance(msg, HumanMessage) else "assistant",
                    "content": msg.content
                }
                for msg in st.session_state.chat_history
            ],
            "timestamp": timestamp,
            "preview": (
                st.session_state.chat_history[0].content[:50] + "..."
                if st.session_state.chat_history and len(st.session_state.chat_history[0].content) > 50
                else (st.session_state.chat_history[0].content if st.session_state.chat_history else "")
            )
        }
        self._save_conversations()

    def _create_new_conversation(self):
        """Cria uma nova conversa em branco."""
        # Verifica se está em processamento antes de criar uma nova conversa
        if st.session_state.processing:
            st.warning("Aguarde a conclusão da resposta atual antes de criar uma nova conversa.", icon="⚠️")
            return
            
        if st.session_state.chat_history:
            self._save_current_conversation()
        st.session_state.current_conversation_id = str(uuid.uuid4())
        st.session_state.chat_history = []

    def _load_conversation(self, conv_id):
        """Carrega uma conversa salva pelo ID."""
        # Verifica se está em processamento antes de carregar a conversa
        if st.session_state.processing:
            st.warning("Aguarde a conclusão da resposta atual antes de carregar outra conversa.", icon="⚠️")
            return
            
        if conv_id not in st.session_state.saved_conversations:
            return
        if st.session_state.chat_history and st.session_state.current_conversation_id != conv_id:
            self._save_current_conversation()
        conversation = st.session_state.saved_conversations[conv_id]
        msgs = []
        for m in conversation["messages"]:
            if m["role"] == "user":
                msgs.append(HumanMessage(content=m["content"]))
            else:
                msgs.append(AIMessage(content=m["content"]))
        st.session_state.chat_history = msgs
        st.session_state.current_conversation_id = conv_id
        
        # Garantir recarregamento da página para atualizar a classe 'active' nos elementos visuais
        st.rerun()

    def _delete_conversation(self, conv_id):
        """Exclui uma conversa do histórico."""
        if conv_id in st.session_state.saved_conversations:
            del st.session_state.saved_conversations[conv_id]
            self._save_conversations()
            if conv_id == st.session_state.current_conversation_id:
                st.session_state.current_conversation_id = str(uuid.uuid4())
                st.session_state.chat_history = []
            st.rerun()

    def _rename_conversation(self, conv_id, new_title):
        """Renomeia o título de uma conversa."""
        if conv_id in st.session_state.saved_conversations:
            # Preservar o timestamp original ao renomear
            original_timestamp = st.session_state.saved_conversations[conv_id].get("timestamp", "")
            
            # Atualizar apenas o título, mantendo o resto das informações inalterado
            st.session_state.saved_conversations[conv_id]["title"] = new_title
            
            # Garantir que o timestamp original seja mantido
            if original_timestamp:
                st.session_state.saved_conversations[conv_id]["timestamp"] = original_timestamp
                
            self._save_conversations()
            st.rerun()

    def _toggle_rename(self, conv_id):
        """Helper para alternar visibilidade do campo de renomeação"""
        if f"show_rename_{conv_id}" not in st.session_state:
            st.session_state[f"show_rename_{conv_id}"] = False
        st.session_state[f"show_rename_{conv_id}"] = not st.session_state[f"show_rename_{conv_id}"]
    
    def _toggle_delete(self, conv_id):
        """Helper para alternar visibilidade da confirmação de exclusão"""
        if f"confirm_delete_{conv_id}" not in st.session_state:
            st.session_state[f"confirm_delete_{conv_id}"] = False
        st.session_state[f"confirm_delete_{conv_id}"] = True

    def render_sidebar(self):
        """Exibe o histórico de conversas na sidebar com design moderno."""
        
        # Cabeçalho da sidebar
        st.sidebar.markdown(f"""
        <div class="sidebar-header">
            <h2>Conversas</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Botão de nova conversa com estilo consistente
        if st.sidebar.button('✨ Nova conversa', key='new_chat', use_container_width=True):
            self._create_new_conversation()
        
        # Adicionar um estilo customizado para o botão
        st.sidebar.markdown("""
        <style>
        /* Estilização para o botão Nova Conversa com a identidade visual */
        button[key="new_chat"] {
            background: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%) !important;
            color: white !important;
            border: none !important;
            padding: 0.8rem 1.2rem !important;
            font-weight: 500 !important;
            margin-bottom: 1.5rem !important;
            box-shadow: 0 4px 12px rgba(109, 29, 122, 0.15) !important;
            transition: all 0.3s ease !important;
            border-radius: 12px !important;
            font-size: 1rem !important;
        }
        
        button[key="new_chat"]:hover {
            box-shadow: 0 6px 18px rgba(109, 29, 122, 0.2) !important;
            transform: translateY(-2px) !important;
            filter: brightness(1.05);
        }
        
        button[key="new_chat"]::before {
            content: "✨ ";
            margin-right: 8px;
        }
        </style>
        
        <script>
        // Script para garantir que textos longos tenham elipses e ajustar posicionamento da data
        document.addEventListener('DOMContentLoaded', function() {
            // Função para aplicar truncamento de texto nos botões de conversas
            function applyTruncation() {
                const cardButtons = document.querySelectorAll('button[key^="card_"]');
                cardButtons.forEach(button => {
                    // Certificar que o botão tenha a classe para truncamento
                    button.classList.add('truncate-text');
                    
                    // Garantir que o texto seja truncado e tenha apenas texto (sem HTML)
                    if (button.textContent && button.textContent.length > 30) {
                        button.setAttribute('title', button.textContent);
                    }
                });
                
                // Posicionar corretamente os badges de data
                document.querySelectorAll('.conversation-date-badge').forEach(badge => {
                    const badgeId = badge.id;
                    if (badgeId && badgeId.startsWith('date-')) {
                        const convId = badgeId.replace('date-', '');
                        const button = document.querySelector(`button[key="card_${convId}"]`);
                        
                        if (button && button.parentElement) {
                            // Ajustar a posição relativa ao pai do botão
                            const buttonContainer = button.parentElement.parentElement;
                            if (buttonContainer) {
                                buttonContainer.style.position = 'relative';
                                badge.style.position = 'absolute';
                                badge.style.right = '10px';
                                badge.style.bottom = '5px';
                                badge.style.zIndex = '5';
                            }
                        }
                    }
                });
            }
            
            // Aplicar o truncamento inicialmente
            setTimeout(applyTruncation, 500);
            
            // Observar mudanças no DOM para replicar o truncamento em novos botões
            const observer = new MutationObserver(applyTruncation);
            observer.observe(document.body, { childList: true, subtree: true });
        });
        </script>
        """, unsafe_allow_html=True)
        
        # Listar conversas salvas ou mostrar estado vazio
        if st.session_state.saved_conversations:
            # Ordenar conversas por timestamp (mais recente primeiro)
            # Importante: Esta ordenação é mantida mesmo quando uma conversa é selecionada
            sorted_convs = sorted(
                st.session_state.saved_conversations.items(),
                key=lambda x: x[1].get("timestamp", ""),
                reverse=True  # Ordem decrescente (mais recente primeiro)
            )
            
            for conv_id, conv_data in sorted_convs:
                title = conv_data.get("title", "Sem título")
                timestamp = conv_data.get("timestamp", "")
                
                # Verificar se é a conversa ativa
                is_active = conv_id == st.session_state.current_conversation_id
                conversation_id = conv_id
                
                # Container para a conversa
                if is_active:
                    # Se for a conversa ativa, adicionar classe CSS
                    st.sidebar.markdown("<div class='conversation-active'>", unsafe_allow_html=True)
                    card_container = st.sidebar.container()
                    st.sidebar.markdown("</div>", unsafe_allow_html=True)
                else:
                    card_container = st.sidebar.container()
                
                # Renderizar o card compacto apenas com título e botões
                with card_container:
                    card_cols = st.columns([5, 1, 1])  # Proporções para título e botões
                    
                    # Coluna para o título
                    with card_cols[0]:
                        # Extrair data formatada para exibir no tooltip
                        try:
                            dt = datetime.datetime.fromisoformat(timestamp)
                            formatted_date = dt.strftime("%d/%m/%Y %H:%M")
                            tooltip = f"Criado em: {formatted_date} - Clique para carregar esta conversa"
                            
                            # Data formatada de forma abreviada para o indicador visual
                            short_date = dt.strftime("%d/%m")
                        except:
                            tooltip = "Clique para carregar esta conversa"
                            short_date = ""
                        
                        # Exibir apenas o título no botão sem HTML adicional
                        if st.button(title, key=f"card_{conv_id}", 
                                  help=tooltip,
                                  use_container_width=True):
                            # Carregar a conversa, sem alterar sua posição na ordenação
                            self._load_conversation(conversation_id)
                        
                        # Após o botão, injetar o badge de data usando um div posicionado
                        if short_date:
                            card_cols[0].markdown(f"""
                            <div class="conversation-date-badge" id="date-{conv_id}">{short_date}</div>
                            """, unsafe_allow_html=True)
                    
                    # Botões de ação em colunas menores
                    with card_cols[1]:
                        if st.button("✏️", key=f"edit_{conv_id}", 
                                  help="Editar título da conversa"):
                            self._toggle_rename(conversation_id)
                    
                    with card_cols[2]:
                        if st.button("🗑️", key=f"delete_{conv_id}", 
                                  help="Excluir conversa"):
                            self._toggle_delete(conversation_id)
                
                # Campo de renomeação (condicional)
                if f"show_rename_{conv_id}" in st.session_state and st.session_state[f"show_rename_{conv_id}"]:
                    with st.sidebar.container():
                        st.markdown('<div class="rename-input">', unsafe_allow_html=True)
                        new_title = st.text_input('Novo título', value=title, key=f"rename_input_{conv_id}")
                        col1, col2 = st.columns([1, 1])
                        with col1:
                            if st.button('Salvar', key=f"save_rename_{conv_id}") and new_title.strip():
                                self._rename_conversation(conv_id, new_title.strip())
                                st.session_state[f"show_rename_{conv_id}"] = False
                        with col2:
                            if st.button('Cancelar', key=f"cancel_rename_{conv_id}"):
                                st.session_state[f"show_rename_{conv_id}"] = False
                        st.markdown('</div>', unsafe_allow_html=True)
                
                # Confirmação de exclusão (condicional)
                if f"confirm_delete_{conv_id}" in st.session_state and st.session_state[f"confirm_delete_{conv_id}"]:
                    with st.sidebar.container():
                        st.warning('Tem certeza que deseja excluir esta conversa?')
                        col1, col2 = st.columns([1, 1])
                        with col1:
                            if st.button('Sim, excluir', key=f"confirm_delete_yes_{conv_id}"):
                                self._delete_conversation(conv_id)
                                st.session_state[f"confirm_delete_{conv_id}"] = False
                        with col2:
                            if st.button('Cancelar', key=f"confirm_delete_no_{conv_id}"):
                                st.session_state[f"confirm_delete_{conv_id}"] = False
        else:
            # Estado vazio - nenhuma conversa
            st.sidebar.markdown("""
            <div class="empty-state">
                <div class="empty-state-icon">💬</div>
                <p>Você ainda não tem conversas salvas.</p>
                <p>Comece uma nova conversa para vê-la aqui!</p>
            </div>
            """, unsafe_allow_html=True)

    def render_header(self):
        st.markdown("""
        <div class="chat-header">
            <h1>CHATSeek</h1>
            <p>Assistente Virtual Inteligente</p>
        </div>
        """, unsafe_allow_html=True)

    def render_chat_messages(self):
        st.markdown("<div class='messages-container'>", unsafe_allow_html=True)
        if not st.session_state.chat_history:
            st.markdown(f"""
            <div class="chat-message assistant-message">
                <div class="message-avatar">🤖</div>
                <div class="message-content">Bem-vindo ao CHATSeek! Como posso ajudar você hoje?</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            for msg in st.session_state.chat_history:
                css_class = "assistant-message" if isinstance(msg, AIMessage) else "user-message"
                content = format_markdown(format_links(msg.content))
                avatar = "🤖" if isinstance(msg, AIMessage) else "👤"
                st.markdown(f"""
                <div class="chat-message {css_class}">
                    <div class="message-avatar">{avatar}</div>
                    <div class="message-content">{content}</div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    def render_chat_input(self):
        # Utiliza o widget nativo do Streamlit sem encapsulá-lo em um container extra
        disabled = st.session_state.processing
        user_input = st.chat_input("Digite sua mensagem...", disabled=disabled)
        if user_input:
            self.handle_user_input(user_input)

    def handle_user_input(self, user_text: str):
        """Processa a mensagem do usuário e gera a resposta (streaming)."""
        user_msg = HumanMessage(content=user_text)
        st.session_state.chat_history.append(user_msg)
        conv_id = st.session_state.current_conversation_id
        self.app.get_session_history(conv_id).add_user_message(user_text)
        
        if 'waiting_response' not in st.session_state:
            st.session_state.waiting_response = False
        st.session_state.waiting_response = True
        
        st.rerun()

    def render(self):
        """Renderiza a aplicação no Streamlit."""
        # Verificação para cancelamento seguro de respostas
        if 'cancel_response' not in st.session_state:
            st.session_state.cancel_response = False
        
        # Garantir que o sistema não fique travado em estado de processamento
        if 'processing_timeout' not in st.session_state:
            st.session_state.processing_timeout = None
            
        # Se está processando há muito tempo, força a liberação
        if st.session_state.processing and st.session_state.processing_timeout:
            current_time = time.time()
            if current_time - st.session_state.processing_timeout > 60:  # 60 segundos de timeout
                st.session_state.processing = False
                st.session_state.processing_timeout = None
                st.warning("O processamento da resposta foi cancelado devido a um tempo limite excedido.", icon="⚠️")
        
        self.render_sidebar()
        self.render_header()
        self.render_chat_messages()
        
        # Processamento de resposta
        if hasattr(st.session_state, 'waiting_response') and st.session_state.waiting_response:
            st.session_state.waiting_response = False
            st.session_state.processing = True
            st.session_state.processing_timeout = time.time()  # Registra o momento do início
            
            last_user_msg = next((msg for msg in reversed(st.session_state.chat_history) 
                                  if isinstance(msg, HumanMessage)), None)
            
            if last_user_msg:
                conv_id = st.session_state.current_conversation_id
                placeholder = st.empty()
                full_response = ""
                
                # Botão para cancelar resposta
                cancel_col1, cancel_col2 = st.columns([4, 1])
                with cancel_col2:
                    if st.button("🛑 Cancelar", key="cancel_generation"):
                        st.session_state.cancel_response = True
                        st.session_state.processing = False
                        st.session_state.processing_timeout = None
                        st.rerun()
                
                placeholder.markdown(
                    """<div class="chat-message assistant-message">
                        <div class="message-avatar">🤖</div>
                        <div class="message-content"><span class="typing-cursor"></span></div>
                    </div>""",
                    unsafe_allow_html=True
                )
                
                try:
                    for chunk in self.app.generate_response(last_user_msg, conv_id):
                        # Verificar se o usuário cancelou a resposta
                        if st.session_state.cancel_response:
                            placeholder.markdown(
                                f"""<div class="chat-message assistant-message">
                                    <div class="message-avatar">🤖</div>
                                    <div class="message-content">Resposta cancelada pelo usuário.</div>
                                </div>""",
                                unsafe_allow_html=True
                            )
                            st.session_state.cancel_response = False
                            break
                            
                        if hasattr(chunk, 'content') and chunk.content:
                            full_response += chunk.content
                            formatted = format_markdown(format_links(full_response))
                            placeholder.markdown(
                                f"""<div class="chat-message assistant-message">
                                    <div class="message-avatar">🤖</div>
                                    <div class="message-content">{formatted}<span class="typing-cursor"></span></div>
                                </div>""",
                                unsafe_allow_html=True
                            )
                            time.sleep(0.08)
                except Exception as e:
                    st.error(f"Erro: {e}")
                    full_response = f"Desculpe, ocorreu um erro: {str(e)}"
                
                # Se resposta não foi cancelada, salva normalmente
                if not st.session_state.cancel_response and full_response:
                    placeholder.markdown(
                        f"""<div class="chat-message assistant-message">
                            <div class="message-avatar">🤖</div>
                            <div class="message-content">{format_markdown(format_links(full_response))}</div>
                        </div>""",
                        unsafe_allow_html=True
                    )
                    
                    ai_msg = AIMessage(content=full_response)
                    st.session_state.chat_history.append(ai_msg)
                    self.app.get_session_history(conv_id).add_ai_message(full_response)
                    if len(st.session_state.chat_history) >= 2:
                        self._save_current_conversation()
            
            st.session_state.processing = False
        
        self.render_chat_input()

def main():
    interface = StreamlitInterface()
    interface.render()

if __name__ == "__main__":
    main()