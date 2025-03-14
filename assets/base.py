def get_base_css():
    return """
/* ======== BASE STYLES ======== */
/* Variáveis CSS */
:root {
    --marca-purple: #6D1D7A;
    --marca-purple-light: rgba(109, 29, 122, 0.05);
    --marca-purple-medium: rgba(109, 29, 122, 0.1);
    --marca-purple-border: rgba(109, 29, 122, 0.2);
    --marca-red: #CC0A2B;
    --marca-red-light: rgba(204, 10, 43, 0.05);
    --marca-red-medium: rgba(204, 10, 43, 0.1);
    --marca-coral: #FF6B6B;
    --gradient-primary: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%);
    --gradient-secondary: linear-gradient(135deg, var(--marca-purple) 0%, var(--marca-red) 100%);
    --gradient-pastel: linear-gradient(135deg, rgba(248, 240, 255, 0.7) 0%, rgba(252, 233, 236, 0.7) 100%);
    --gradient-subtle: linear-gradient(135deg, rgba(109, 29, 122, 0.05) 0%, rgba(204, 10, 43, 0.02) 100%);
    --chat-user: linear-gradient(135deg, #FFE5E5 0%, #FFFAFA 100%);
    --chat-assistant: linear-gradient(135deg, #F8F0FF 0%, #FCE9EC 100%);
    --text-primary: #333333;
    --text-secondary: #666666;
    --text-tertiary: #888888;
    --text-light: #999999;
    --bg-light: #F9F7FA;
    --bg-purple-soft: rgba(109, 29, 122, 0.03);
    --bg-red-soft: rgba(204, 10, 43, 0.02);
    --accent-purple: rgba(109, 29, 122, 0.7);
    --accent-red: rgba(204, 10, 43, 0.7);
    --shadow-sm: 0 2px 8px rgba(109, 29, 122, 0.06);
    --shadow-md: 0 4px 12px rgba(109, 29, 122, 0.08);
    --shadow-lg: 0 6px 18px rgba(109, 29, 122, 0.12);
    --shadow-xl: 0 8px 24px rgba(109, 29, 122, 0.18);
    --shadow-primary: 0 4px 6px -1px rgba(109, 29, 122, 0.1);
    --radius-sm: 6px;
    --radius-md: 12px;
    --radius-lg: 24px;
    --transition-fast: all 0.2s ease;
    --transition-normal: all 0.3s ease;
    --spacing-card: 8px;
    --font-primary: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

/* Reset global */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Estilo base */
body {
    font-family: var(--font-primary);
    background-color: var(--bg-light) !important;
    color: var(--text-primary);
    line-height: 1.6;
}

/* Remover margem do footer do Streamlit */
footer {
    display: none !important;
}

/* Customização do bloco de código */
code {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
}

/* Customização dos links */
a {
    color: var(--marca-purple);
    text-decoration: none;
    transition: all 0.2s ease;
}

a:hover {
    color: var(--marca-red);
    text-decoration: underline;
}

/* Customização do scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: rgba(109, 29, 122, 0.3);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(109, 29, 122, 0.5);
}

/* Container principal - aumentar max-width */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, rgba(109, 29, 122, 0.03) 0%, rgba(255, 255, 255, 1) 100%);
}

/* Ajustes de tamanho para o conteúdo principal */
[data-testid="stAppViewContainer"] > .main {
    max-width: 1200px !important;
}

/* Remover padding do header */
[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Estilizar botões do Streamlit */
button[kind="primary"] {
    background: var(--gradient-primary) !important;
    border: none !important;
}

/* Animação suave de transição para todos os elementos */
.stButton, .stTextInput, .stSelectbox, input, button {
    transition: all 0.3s ease !important;
}

/* Ajuste para o menu hamburger */
[data-testid="baseButton-headerNoPadding"] {
    color: var(--marca-purple) !important;
}

/* Estilo para widgets de entrada */
[data-testid="stTextInput"] > div:first-child {
    border-radius: var(--radius-md) !important;
}

/* Ajuste responsivo para dispositivos móveis */
@media (max-width: 768px) {
    [data-testid="stSidebar"] {
        min-width: 100% !important;
    }
    
    [data-testid="stAppViewContainer"] > .main {
        padding: 1rem !important;
    }
}
"""