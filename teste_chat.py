import streamlit as st
import base64
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="BradSeek | Assistência Inteligente",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para um visual mais sofisticado e moderno
css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --marca-red: #CC0A2B;
        --marca-purple: #6D1D7A;
        --marca-pink: #F06292;
        --marca-light: #F5F5F7;
        --text-dark: #1D1D1F;
        --text-medium: #494953;
        --text-light: #86868B;
        --background-white: #FFFFFF;
        --input-bg: #F5F5F7;
        --gradient-primary: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%);
        --gradient-button: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-pink) 100%);
        --shadow-soft: 0 10px 30px -5px rgba(0, 0, 0, 0.05);
        --shadow-elevated: 0 20px 40px -5px rgba(0, 0, 0, 0.1);
        --radius-sm: 8px;
        --radius-md: 16px;
        --radius-lg: 24px;
        --transition-smooth: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    
    body {
        font-family: 'Inter', sans-serif;
        background-color: var(--background-white);
        color: var(--text-dark);
        line-height: 1.6;
    }
    
    .stApp {
        background-color: var(--background-white);
    }
    
    /* Estilo do contêiner principal */
    .container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    /* Tipografia */
    h1 {
        font-weight: 700;
        font-size: 2.5rem;
        letter-spacing: -0.03em;
        margin-bottom: 1rem;
    }
    
    h2 {
        font-weight: 600;
        font-size: 1.8rem;
        letter-spacing: -0.02em;
        margin-bottom: 1rem;
    }
    
    h3 {
        font-weight: 600;
        font-size: 1.4rem;
        letter-spacing: -0.01em;
    }
    
    p {
        font-weight: 400;
        color: var(--text-medium);
        max-width: 650px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .highlight {
        color: var(--marca-purple);
        font-weight: 600;
    }
    
    .gradient-text {
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }
    
    /* Estilo do cartão */
    .card {
        background-color: var(--background-white);
        border-radius: var(--radius-lg);
        padding: 2.5rem;
        box-shadow: var(--shadow-soft);
        transition: var(--transition-smooth);
        margin-bottom: 2rem;
        border: 1px solid rgba(0,0,0,0.03);
    }
    
    .card:hover {
        box-shadow: var(--shadow-elevated);
        transform: translateY(-2px);
    }
    
    /* Estilo do logo */
    .logo-container {
        margin-bottom: 2.5rem;
        text-align: center;
    }
    
    .logo-inner {
        display: inline-block;
        padding: 1rem 2rem;
        border-radius: var(--radius-md);
        background-color: white;
        box-shadow: var(--shadow-soft);
    }
    
    /* Cartão de boas-vindas */
    .welcome-card {
        text-align: center;
        padding: 3rem 2rem;
        animation: fadeIn 0.8s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Indicador de progresso */
    .progress-container {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    
    .progress-step {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin: 0 5px;
        background-color: #E0E0E0;
        transition: var(--transition-smooth);
    }
    
    .progress-step.active {
        background: var(--gradient-primary);
        transform: scale(1.2);
    }
    
    /* Estilo do formulário */
    .form-container {
        max-width: 650px;
        margin: 0 auto;
        animation: slideUp 0.6s ease-out;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stTextInput > div > div > input {
        border-radius: var(--radius-sm);
        border: none;
        background-color: var(--input-bg);
        padding: 1rem 1.2rem;
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        transition: var(--transition-smooth);
    }
    
    .stTextInput > div > div > input:focus {
        box-shadow: 0 0 0 2px rgba(109, 29, 122, 0.2);
        background-color: white;
    }
    
    /* Estilo do botão */
    .stButton > button {
        background: var(--gradient-button);
        color: white;
        border: none;
        padding: 0.75rem 2.5rem;
        border-radius: var(--radius-sm);
        font-weight: 600;
        font-size: 1rem;
        letter-spacing: 0.01em;
        transition: var(--transition-smooth);
        box-shadow: 0 4px 10px rgba(204, 10, 43, 0.25);
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(204, 10, 43, 0.3);
    }
    
    .stButton > button:active {
        transform: translateY(1px);
    }
    
    /* Mensagem de sucesso */
    .success-message {
        text-align: center;
        padding: 2rem;
        border-radius: var(--radius-md);
        background: linear-gradient(135deg, #F7FFF7 0%, #EAFDE9 100%);
        border: 1px solid #CCEBC5;
        margin-top: 2rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(114, 196, 121, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(114, 196, 121, 0); }
        100% { box-shadow: 0 0 0 0 rgba(114, 196, 121, 0); }
    }
    
    /* Mensagem de erro */
    .error-message {
        border-radius: var(--radius-sm);
        background-color: #FFEBEE;
        border: 1px solid #FFCDD2;
        padding: 1rem;
        margin-top: 1rem;
        color: #D32F2F;
    }
    
    /* Rodapé */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid #F0F0F0;
        color: var(--text-light);
        font-size: 0.9rem;
    }
    
    /* Estilo de campo de formulário personalizado */
    .custom-field {
        position: relative;
        margin-bottom: 1.5rem;
    }
    
    .field-icon {
        position: absolute;
        left: 1rem;
        top: 50%;
        transform: translateY(-50%);
        color: var(--text-light);
    }
    
    /* Consultas de mídia para responsividade */
    @media (max-width: 768px) {
        .card {
            padding: 1.5rem;
        }
        
        h1 {
            font-size: 2rem;
        }
        
        h2 {
            font-size: 1.5rem;
        }
    }
</style>
"""

# Injetar CSS
st.markdown(css, unsafe_allow_html=True)

# Inicializar estado da sessão
if 'stage' not in st.session_state:
    st.session_state.stage = 1
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}
if 'submit_time' not in st.session_state:
    st.session_state.submit_time = None

# Funções de navegação
def next_stage():
    st.session_state.stage += 1

def previous_stage():
    st.session_state.stage -= 1

def submit_form(form_data):
    st.session_state.form_data = form_data
    st.session_state.submit_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    next_stage()

# HTML do logo com animação
def get_logo_html():
    logo_html = """
    <div class="logo-container">
        <div class="logo-inner">
            <h1 class="gradient-text">BradSeek</h1>
        </div>
    </div>
    """
    return logo_html

# Indicador de progresso
def progress_indicator(current_stage, total_stages=3):
    html = """
    <div class="progress-container">
    """
    for i in range(1, total_stages + 1):
        if i == current_stage:
            html += '<div class="progress-step active"></div>'
        else:
            html += '<div class="progress-step"></div>'
    html += "</div>"
    return html

# Contêiner principal
st.markdown('<div class="container">', unsafe_allow_html=True)

# Logo
st.markdown(get_logo_html(), unsafe_allow_html=True)

# Indicador de progresso
st.markdown(progress_indicator(st.session_state.stage), unsafe_allow_html=True)

# Etapa 1: Página de boas-vindas
if st.session_state.stage == 1:
    st.markdown("""
    <div class="card welcome-card">
        <h1>Bem-vindo ao <span class="gradient-text">BradSeek</span></h1>
        <p>Agradecemos seu interesse em nosso assistente de chat AI avançado. Estamos empolgados para ajudá-lo a desbloquear nova produtividade e insights.</p>
        <p>No <span class="highlight">BradSeek</span>, estamos comprometidos em fornecer soluções inteligentes que simplificam tarefas complexas e melhoram seu fluxo de trabalho diário.</p>
        <p>Complete seu registro em apenas alguns passos para ganhar acesso.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("Começar", on_click=next_stage)

# Etapa 2: Formulário de registro
elif st.session_state.stage == 2:
    st.markdown("""
    <div class="card">
        <h2>Complete Seu Perfil</h2>
        <p>Por favor, forneça as seguintes informações para finalizar seu acesso ao BradSeek.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("registration_form", clear_on_submit=False):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        name = st.text_input("Nome Completo", placeholder="Digite seu nome completo")
        employee_id = st.text_input("ID do Funcionário", placeholder="Digite seu ID de funcionário")
        email = st.text_input("Email de Trabalho", placeholder="Digite seu email de trabalho")
        department = st.selectbox("Departamento", ["", "Finanças", "Marketing", "TI", "RH", "Operações", "Vendas", "Outro"])
        purpose = st.text_area("Como você planeja usar o BradSeek?", placeholder="Descreva brevemente seu uso pretendido", max_chars=200)
        
        terms_agree = st.checkbox("Eu concordo com os termos de serviço e a política de privacidade")
        
        submit_button = st.form_submit_button("Completar Registro")
        
        if submit_button:
            if name and employee_id and email and department and terms_agree:
                form_data = {
                    "name": name,
                    "employee_id": employee_id,
                    "email": email,
                    "department": department,
                    "purpose": purpose
                }
                submit_form(form_data)
            else:
                st.markdown("""
                <div class="error-message">
                    Por favor, complete todos os campos obrigatórios e aceite os termos para continuar.
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("Voltar", on_click=previous_stage)

# Etapa 3: Página de confirmação
elif st.session_state.stage == 3:
    st.markdown("""
    <div class="card welcome-card">
        <h2>Registro Completo! 🎉</h2>
        <p>Obrigado por completar seu registro no BradSeek.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card">
        <h3>Detalhes do Registro</h3>
        <p><strong>Nome:</strong> {st.session_state.form_data.get('name', '')}</p>
        <p><strong>ID do Funcionário:</strong> {st.session_state.form_data.get('employee_id', '')}</p>
        <p><strong>Email:</strong> {st.session_state.form_data.get('email', '')}</p>
        <p><strong>Departamento:</strong> {st.session_state.form_data.get('department', '')}</p>
        <p><strong>Enviado em:</strong> {st.session_state.submit_time}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Opção para voltar ao formulário de registro
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("Recomeçar", on_click=lambda: setattr(st.session_state, 'stage', 1))