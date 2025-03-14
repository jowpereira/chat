def get_sidebar_css():
    return """
/* ======== VARIÁVEIS ======== */
:root {
    --marca-purple: #6D1D7A;
    --marca-red: #CC0A2B;
    --marca-coral: #FF6B6B;
    --gradient-primary: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%);
    --gradient-secondary: linear-gradient(135deg, var(--marca-purple) 0%, var(--marca-red) 100%);
    --gradient-pastel: linear-gradient(135deg, rgba(109, 29, 122, 0.15) 0%, rgba(204, 10, 43, 0.12) 100%);
    --gradient-subtle: linear-gradient(135deg, rgba(109, 29, 122, 0.05) 0%, rgba(204, 10, 43, 0.02) 100%);
    --chat-user: linear-gradient(135deg, #FFE5E5 0%, #FFFAFA 100%);
    --chat-assistant: linear-gradient(135deg, #F8F0FF 0%, #FCE9EC 100%);
    --shadow-sm: 0 2px 8px rgba(109, 29, 122, 0.06);
    --shadow-md: 0 4px 12px rgba(109, 29, 122, 0.08);
    --shadow-lg: 0 6px 18px rgba(109, 29, 122, 0.12);
    --shadow-primary: 0 4px 6px -1px rgba(109, 29, 122, 0.1);
    --transition-fast: all 0.2s ease;
    --transition-normal: all 0.3s ease;
}

/* ======== ESTILOS DA SIDEBAR ======== */
/* Reset básico para garantir compatibilidade */
*, *::before, *::after {
    box-sizing: border-box;
}

/* Estilos de layout para a sidebar */
section[data-testid="stSidebar"] {
    background-color: white !important;
    border-right: 1px solid rgba(109, 29, 122, 0.15) !important;
    box-shadow: var(--shadow-md) !important;
    transition: var(--transition-normal);
}

section[data-testid="stSidebar"] > div:first-child {
    background-color: white !important;
    background-image: linear-gradient(180deg, rgba(109, 29, 122, 0.04) 0%, rgba(204, 10, 43, 0.02) 100%) !important;
}

[data-testid="stSidebarUserContent"] {
    padding-top: 0 !important;
}

section[data-testid="stSidebar"] [data-testid="column"] {
    padding: 0 !important;
}

/* Estilização dos botões na sidebar */
section[data-testid="stSidebar"] .stButton > button {
    border-radius: 12px !important;
    transition: var(--transition-normal) !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
    box-shadow: var(--shadow-sm) !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-md) !important;
}

/* Estilização do header da sidebar */
.sidebar-header {
    background: linear-gradient(180deg, rgba(248, 240, 255, 0.8) 0%, rgba(255, 255, 255, 0) 100%);
    padding: 1.8rem 1rem 1.2rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid rgba(109, 29, 122, 0.15);
    box-shadow: 0 6px 16px -10px rgba(109, 29, 122, 0.12);
    position: relative;
}

.sidebar-header::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%);
    z-index: 1;
}

.sidebar-header h2 {
    font-weight: 700;
    font-size: 1.6rem;
    letter-spacing: -0.5px;
    margin: 0.5rem 0;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    color: transparent;
    text-align: center;
    position: relative;
    text-shadow: 0 2px 4px rgba(109, 29, 122, 0.08);
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.sidebar-header h2::before {
    content: "";
    width: 35px;
    height: 35px;
    margin-right: 10px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%236D1D7A"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2m0 14H5.2L4 17.2V4h16v12m-3-5h-2V9h2m-4 2h-2V9h2m-4 2H7V9h2"/></svg>');
    background-repeat: no-repeat;
    background-position: center;
    background-size: contain;
    filter: drop-shadow(0 2px 3px rgba(109, 29, 122, 0.15));
    transition: transform 0.3s ease;
}

.sidebar-header h2:hover::before {
    transform: scale(1.1);
}

/* Estilização da área de histórico de conversas */
div.conversation-container {
    background: white;
    border-radius: 14px;
    box-shadow: var(--shadow-sm);
    margin-bottom: 12px;
    padding: 12px 16px;
    cursor: pointer;
    position: relative;
    border: 1px solid rgba(109, 29, 122, 0.08);
    transition: all 0.3s ease;
    overflow: hidden;
}

div.conversation-container:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
    border-color: rgba(109, 29, 122, 0.15);
}

div.conversation-container.active {
    background: var(--gradient-subtle);
    border-color: rgba(109, 29, 122, 0.2);
    box-shadow: var(--shadow-md);
}

div.conversation-container::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 4px;
    background: var(--gradient-primary);
    opacity: 0;
    transition: all 0.3s ease;
}

div.conversation-container:hover::before {
    opacity: 0.6;
}

div.conversation-container.active::before {
    opacity: 1;
}

div.conversation-container::after {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    width: 40px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.8));
    opacity: 0;
    transition: opacity 0.3s ease;
}

div.conversation-container:hover::after {
    opacity: 0.6;
}

div.conversation-container.active::after {
    opacity: 0;
}

/* Estilização dos componentes nas conversas */
.conversation-title {
    font-weight: 600;
    font-size: 1rem;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    letter-spacing: -0.2px;
    position: relative;
}

.conversation-title::after {
    content: "";
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 30px;
    height: 2px;
    background: var(--gradient-primary);
    opacity: 0;
    transform: scaleX(0);
    transform-origin: left;
    transition: all 0.3s ease;
    border-radius: 2px;
}

div.conversation-container:hover .conversation-title::after,
div.conversation-container.active .conversation-title::after {
    opacity: 0.7;
    transform: scaleX(1);
}

.conversation-preview {
    font-size: 0.85rem;
    color: var(--text-secondary);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    line-height: 1.5;
    background: linear-gradient(to bottom, var(--text-secondary), var(--text-tertiary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

div.conversation-container.active .conversation-preview {
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 500;
}

.conversation-date {
    font-size: 0.75rem;
    color: #888;
    text-align: right;
    font-style: italic;
    letter-spacing: 0.2px;
}

/* Estilização dos botões de ação */
.actions-container .stButton > button {
    font-size: 0.85rem !important;
    padding: 0.5rem 0.8rem !important;
    min-height: 0 !important;
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    border-radius: 8px !important;
    transition: var(--transition-fast) !important;
}

.actions-container [data-testid="column"]:nth-child(1) .stButton > button {
    color: var(--marca-purple) !important;
    background: rgba(109, 29, 122, 0.1) !important;
    font-weight: 500 !important;
}

.actions-container [data-testid="column"]:nth-child(2) .stButton > button {
    color: #555 !important;
    background: rgba(0, 0, 0, 0.05) !important;
}

.actions-container [data-testid="column"]:nth-child(3) .stButton > button {
    color: var(--marca-red) !important;
    background: rgba(204, 10, 43, 0.08) !important;
}

.actions-container .stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-sm) !important;
}

.actions-container [data-testid="column"]:nth-child(1) .stButton > button:hover {
    background: rgba(109, 29, 122, 0.15) !important;
}

.actions-container [data-testid="column"]:nth-child(2) .stButton > button:hover {
    background: rgba(0, 0, 0, 0.08) !important;
}

.actions-container [data-testid="column"]:nth-child(3) .stButton > button:hover {
    background: rgba(204, 10, 43, 0.12) !important;
}

/* Estado vazio */
.empty-state {
    text-align: center;
    padding: 3.2rem 1.6rem;
    color: #444;
    font-size: 0.95rem;
    border: none;
    border-radius: 18px;
    margin: 2rem 1.5rem;
    background: linear-gradient(165deg, rgba(249, 245, 252, 0.9) 0%, rgba(255, 255, 255, 0.9) 100%);
    box-shadow: 0 8px 18px rgba(109, 29, 122, 0.06);
    transition: var(--transition-normal);
    position: relative;
    overflow: hidden;
}

.empty-state::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--gradient-pastel);
    border-radius: 18px 18px 0 0;
    opacity: 0.8;
}

.empty-state::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 18px;
    padding: 1px;
    background: linear-gradient(135deg, rgba(109, 29, 122, 0.15), rgba(204, 10, 43, 0.15), rgba(109, 29, 122, 0.15));
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
    opacity: 0.6;
}

.empty-state:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 24px rgba(109, 29, 122, 0.08);
}

.empty-state:hover::after {
    opacity: 0.8;
}

.empty-state-icon {
    position: relative;
    font-size: 3.6rem;
    margin-bottom: 1.4rem;
    opacity: 0.8;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    color: transparent;
    filter: drop-shadow(0 3px 5px rgba(109, 29, 122, 0.15));
    display: inline-block;
}

.empty-state p {
    margin-bottom: 1rem;
    line-height: 1.8;
    max-width: 280px;
    margin-left: auto;
    margin-right: auto;
    color: #444;
}

.empty-state p strong {
    color: var(--marca-purple);
    font-weight: 600;
}

/* Novo botão de conversa */
.new-chat-btn {
    background: var(--gradient-primary) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(109, 29, 122, 0.25) !important;
    margin-bottom: 1.5rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
    padding: 0.7rem 1.2rem !important;
    position: relative;
    overflow: hidden;
}

.new-chat-btn::before {
    content: "+";
    font-size: 1.2rem;
    margin-right: 8px;
    font-weight: 700;
}

.new-chat-btn:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 6px 16px rgba(109, 29, 122, 0.35) !important;
}

.new-chat-btn::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0) 100%);
    transform: translateX(-100%);
    transition: transform 0.7s ease;
}

.new-chat-btn:hover::after {
    transform: translateX(100%);
}

/* Ajustes responsivos */
@media (max-width: 992px) {
    section[data-testid="stSidebar"] {
        min-width: 280px !important;
        max-width: 350px !important;
    }
    
    .sidebar-header h2 {
        font-size: 1.4rem;
    }
    
    .sidebar-header h2::before {
        font-size: 1.3rem;
    }
}

@media (min-width: 993px) {
    section[data-testid="stSidebar"] {
        min-width: 320px !important;
        max-width: 400px !important;
    }
}

/* ======== FIM ESTILOS DA SIDEBAR ======== */
"""