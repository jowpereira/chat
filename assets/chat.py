def get_chat_css():
    return """
/* Cabeçalho */
.chat-header {
    text-align: center;
    margin-bottom: 2rem;
    padding: 1.8rem 0 1.5rem;
    background: linear-gradient(135deg, rgba(109, 29, 122, 0.05) 0%, rgba(204, 10, 43, 0.02) 100%);
    border-radius: 0 0 30px 30px;
    border-bottom: 1px solid rgba(109, 29, 122, 0.08);
    box-shadow: 0 6px 18px -8px rgba(109, 29, 122, 0.08);
    position: relative;
    overflow: hidden;
}

.chat-header::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--gradient-primary);
    z-index: 1;
}

.chat-header::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 50% 0%, rgba(109, 29, 122, 0.1) 0%, transparent 70%);
    pointer-events: none;
}

.chat-header h1 {
    margin: 0.5rem 0;
    font-weight: 800;
    font-size: 2.7rem;
    letter-spacing: -1.5px;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    color: transparent;
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    text-shadow: 0 2px 4px rgba(109, 29, 122, 0.12);
    filter: drop-shadow(0 2px 3px rgba(0, 0, 0, 0.04));
    transition: transform 0.3s ease;
}

.chat-header h1:hover {
    transform: translateY(-2px);
}

.chat-header h1::before {
    content: "🤖";
    display: flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    margin-right: 12px;
    font-size: 32px;
    background: linear-gradient(145deg, rgba(109, 29, 122, 0.7) 0%, rgba(156, 46, 161, 0.6) 100%);
    border-radius: 50%;
    color: white;
    filter: drop-shadow(0 2px 3px rgba(109, 29, 122, 0.2));
    transition: transform 0.3s ease;
    border: 1.5px solid rgba(255, 255, 255, 0.9);
}

.chat-header h1:hover::before {
    transform: scale(1.1) rotate(5deg);
}

.chat-header p {
    color: #555;
    margin-bottom: 0.5rem;
    font-size: 1.15rem;
    font-weight: 300;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.4;
}

/* Container de mensagens */
.messages-container {
    margin: 0 auto;
    max-width: 850px;
    width: 100%;
    padding: 0 1rem;
}

/* Layout da mensagem com avatar lateral */
.chat-message {
    display: flex;
    margin: 32px 0;
    position: relative;
    align-items: flex-start;
}

/* Estilos para o avatar */
.message-avatar {
    font-size: 1.6rem;
    line-height: 1;
    margin-right: 12px;
    margin-top: 0;
    height: 48px;
    width: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: transform 0.3s ease;
}

.chat-message:hover .message-avatar {
    transform: scale(1.03);
}

/* Conteúdo da mensagem */
.message-content {
    flex: 1;
    padding: 1.2rem 1.4rem;
    border-radius: 0 18px 18px 18px;
    line-height: 1.6;
    font-size: 1rem;
    color: #333;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    position: relative;
    transition: all 0.3s ease;
    overflow-wrap: break-word;
    word-wrap: break-word;
    hyphens: auto;
    transform-origin: top left;
}

.chat-message:hover .message-content {
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
}

/* Melhorias para blocos de código */
.message-content pre {
    background-color: #1e1e1e;
    padding: 14px;
    border-radius: 12px;
    margin: 14px 0;
    overflow-x: auto;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    position: relative;
}

.message-content pre::before {
    content: "código";
    position: absolute;
    top: 0;
    right: 0;
    background: linear-gradient(135deg, var(--marca-purple) 0%, var(--marca-red) 100%);
    color: white;
    font-size: 0.7rem;
    padding: 0.2rem 0.5rem;
    border-radius: 0 8px 0 8px;
    opacity: 0.8;
    text-transform: uppercase;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.message-content pre code {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    color: #f8f8f8;
    white-space: pre;
    display: block;
    font-size: 0.9em;
    line-height: 1.5;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.message-content code {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    background-color: rgba(109, 29, 122, 0.1);
    padding: 3px 6px;
    border-radius: 4px;
    font-size: 0.9em;
    color: var(--marca-purple);
    font-weight: 500;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(109, 29, 122, 0.1);
    white-space: nowrap;
}

/* Estilos para mensagem do assistente */
.assistant-message {
    flex-direction: row;
    animation: message-in-left 0.3s ease forwards;
}

.assistant-message .message-avatar {
    background: linear-gradient(145deg, rgba(109, 29, 122, 0.7) 0%, rgba(156, 46, 161, 0.6) 100%);
    color: white;
    box-shadow: 0 4px 10px rgba(109, 29, 122, 0.08);
    border: 1.5px solid rgba(255, 255, 255, 0.9);
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
}

.assistant-message .message-avatar::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.22) 0%, transparent 70%);
    pointer-events: none;
}

.assistant-message .message-avatar::after {
    display: none;
}

.assistant-message .message-content {
    background: linear-gradient(145deg, rgba(109, 29, 122, 0.05) 0%, rgba(109, 29, 122, 0.02) 100%);
    border: 1px solid rgba(109, 29, 122, 0.1);
    border-radius: 0 18px 18px 18px;
    box-shadow: 0 4px 12px rgba(109, 29, 122, 0.05);
}

.assistant-message .message-content::before {
    content: "";
    position: absolute;
    left: -10px;
    top: 20px;
    width: 18px;
    height: 18px;
    background: linear-gradient(135deg, rgba(109, 29, 122, 0.05) 0%, rgba(109, 29, 122, 0.02) 100%);
    transform: rotate(45deg);
    border-left: 1px solid rgba(109, 29, 122, 0.1);
    border-bottom: 1px solid rgba(109, 29, 122, 0.1);
    z-index: -1;
}

/* Estilos para mensagem do usuário */
.user-message {
    flex-direction: row-reverse;
    animation: message-in-right 0.3s ease forwards;
}

.user-message .message-avatar {
    margin-right: 0;
    margin-left: 12px;
    background: linear-gradient(145deg, rgba(204, 10, 43, 0.5) 0%, rgba(255, 107, 107, 0.4) 100%);
    color: white;
    box-shadow: 0 4px 10px rgba(204, 10, 43, 0.06);
    border: 1.5px solid var(--marca-coral);
    opacity: 0.8;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
}

.user-message .message-avatar::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 70% 70%, rgba(255, 255, 255, 0.22) 0%, transparent 70%);
    pointer-events: none;
}

.user-message .message-avatar::after {
    display: none;
}

.user-message .message-content {
    background: linear-gradient(145deg, rgba(204, 10, 43, 0.02) 0%, rgba(255, 107, 107, 0.01) 100%);
    border: 1px solid rgba(204, 10, 43, 0.05);
    border-radius: 18px 0 18px 18px;
    box-shadow: 0 4px 12px rgba(204, 10, 43, 0.02);
}

.user-message .message-content::before {
    content: "";
    position: absolute;
    right: -10px;
    top: 20px;
    width: 18px;
    height: 18px;
    background: linear-gradient(135deg, rgba(204, 10, 43, 0.03) 0%, rgba(204, 10, 43, 0.01) 100%);
    transform: rotate(45deg);
    border-right: 1px solid rgba(204, 10, 43, 0.08);
    border-top: 1px solid rgba(204, 10, 43, 0.08);
    z-index: -1;
}

/* Estilo do input do chat */
.chat-input-container {
    position: fixed !important;
    bottom: 20px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 85% !important;
    max-width: 850px !important;
    background: white !important;
    box-shadow: 0 6px 20px rgba(109, 29, 122, 0.08) !important;
    padding: 16px 22px !important;
    z-index: 999 !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    border-radius: 28px !important;
    border: 1px solid rgba(109, 29, 122, 0.06) !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    background-color: rgba(255, 255, 255, 0.98) !important;
}

.chat-input-container::before {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 28px;
    padding: 1px;
    background: linear-gradient(90deg, rgba(109, 29, 122, 0.12), rgba(204, 10, 43, 0.12));
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.chat-input-container:hover {
    box-shadow: 0 8px 22px rgba(109, 29, 122, 0.12) !important;
    transform: translateX(-50%) translateY(-2px) !important;
}

.chat-input-container:hover::before {
    opacity: 0.8;
}

/* Aplicar estilo ao input do Streamlit */
[data-testid="stChatInput"] {
    width: 100% !important;
}

/* Estilizar o campo de texto e o botão de envio */
[data-testid="stChatInput"] > div {
    border-radius: 18px !important;
    border: 1px solid #E0E0E0 !important;
    background-color: rgba(248, 240, 255, 0.25) !important;
    transition: all 0.3s ease !important;
    padding: 6px 12px !important;
    overflow: hidden !important;
    height: 44px !important;
    display: flex !important;
    align-items: center !important;
}

[data-testid="stChatInput"] > div:focus-within {
    border-color: var(--marca-purple) !important;
    box-shadow: 0 0 0 1px rgba(109, 29, 122, 0.08) !important;
    background-color: rgba(255, 255, 255, 0.95) !important;
}

[data-testid="stChatInput"] > div:hover {
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05) !important;
    border-color: #D0D0D0 !important;
}

/* Estilizar o botão de envio */
[data-testid="stChatInput"] button {
    background: linear-gradient(120deg, var(--marca-purple) 0%, rgba(156, 46, 161, 0.9) 100%) !important;
    border-radius: 50% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 3px 8px rgba(109, 29, 122, 0.08) !important;
    margin-left: 8px !important;
    width: 38px !important;
    height: 38px !important;
    min-height: 38px !important;
    max-height: 38px !important;
    padding: 8px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    overflow: hidden !important;
}

[data-testid="stChatInput"] button::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at center, rgba(255, 255, 255, 0.3) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

[data-testid="stChatInput"] button::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(120deg, transparent 30%, rgba(255, 255, 255, 0.15), transparent 70%);
    transform: translateX(-100%);
    transition: transform 0.6s ease;
    pointer-events: none;
}

[data-testid="stChatInput"] button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 5px 12px rgba(109, 29, 122, 0.15) !important;
}

[data-testid="stChatInput"] button:hover::before {
    opacity: 1;
}

[data-testid="stChatInput"] button:hover::after {
    transform: translateX(100%);
}

/* Estilo de placeholder */
[data-testid="stChatInput"] input {
    font-size: 0.95rem !important;
    letter-spacing: 0.2px !important;
}

/* Cursor de digitação */
.typing-cursor {
    display: inline-block;
    width: 2px;
    height: 1em;
    background: var(--marca-purple);
    vertical-align: bottom;
    animation: blink 1s infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}

/* Ajustes para visualização em dispositivos móveis */
@media (max-width: 768px) {
    .chat-header h1 {
        font-size: 2.2rem;
    }
    
    .chat-header h1::before {
        font-size: 2rem;
        margin-right: 8px;
    }
    
    .chat-header p {
        font-size: 1rem;
        padding: 0 15px;
    }
    
    .chat-input-container {
        width: 95% !important;
        padding: 12px 16px !important;
        bottom: 15px !important;
    }
    
    .message-avatar {
        font-size: 1.5rem;
        height: 40px;
        width: 40px;
    }
    
    .message-content {
        padding: 1rem 1.2rem;
        font-size: 0.95rem;
    }
}

/* Adicionar animação sutis para chegada de mensagens */
@keyframes message-in-left {
    0% { opacity: 0; transform: translateX(-20px); }
    100% { opacity: 1; transform: translateX(0); }
}

@keyframes message-in-right {
    0% { opacity: 0; transform: translateX(20px); }
    100% { opacity: 1; transform: translateX(0); }
}

.assistant-message:hover .message-content {
    transform: translateY(-2px) scale(1.005);
}

.user-message:hover .message-content {
    transform: translateY(-2px) scale(1.005);
}
"""