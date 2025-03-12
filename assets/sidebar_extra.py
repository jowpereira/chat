def get_sidebar_extra_css():
    return """
    /* Estilos para a sidebar com cards compactos modernos */
    
    /* Container geral para o conjunto do card */
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"]) {
        background: linear-gradient(135deg, rgba(248, 240, 255, 0.5) 0%, rgba(252, 233, 236, 0.5) 100%);
        border-radius: 10px;
        border: 1px solid rgba(109, 29, 122, 0.25);
        margin-bottom: var(--spacing-card); /* Usando o espaçamento padronizado */
        position: relative;
        transition: all 0.3s ease;
        box-shadow: 0 2px 6px rgba(109, 29, 122, 0.12);
        overflow: hidden; /* Mantém todos os elementos contidos no card */
        min-height: 29px;
        height: 29px; /* Redução de 10% dos 32px */
        max-height: 29px;
        display: flex;
        align-items: center;
    }
    
    /* Card normal em hover - efeito suave */
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"]):hover {
        box-shadow: 0 3px 10px rgba(109, 29, 122, 0.2); 
        border-color: rgba(109, 29, 122, 0.5);
        transform: scale(1.01); 
        background: linear-gradient(135deg, rgba(248, 240, 255, 0.8) 0%, rgba(252, 233, 236, 0.8) 100%);
    }
    
    /* Destacar conversa ativa com cores da marca - MUITO mais intenso */
    .conversation-active div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"]) {
        border: none;
        background: linear-gradient(135deg, rgba(109, 29, 122, 0.25) 0%, rgba(204, 10, 43, 0.25) 100%);
        box-shadow: 0 4px 14px rgba(109, 29, 122, 0.2); 
        position: relative;
        overflow: hidden;
        transform: translateY(-1px) scale(1.02);
        z-index: 10;
    }
    
    /* Adicionar borda com gradiente ao card ativo */
    .conversation-active div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"])::before {
        content: "";
        position: absolute;
        inset: 0;
        padding: 2px;
        border-radius: 10px;
        background: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%);
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 1;
        z-index: 1;
    }
    
    /* Marcador lateral para o card ativo */
    .conversation-active div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"])::after {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 3px; /* Reduzido de 4px */
        height: 100%;
        background: linear-gradient(to bottom, var(--marca-red), var(--marca-purple));
        opacity: 1;
        z-index: 2;
    }
    
    /* Efeito sutil no card ativo ao passar mouse */
    .conversation-active div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"]):hover {
        box-shadow: 0 5px 18px rgba(109, 29, 122, 0.25);
        background: linear-gradient(135deg, rgba(109, 29, 122, 0.3) 0%, rgba(204, 10, 43, 0.3) 100%);
        transform: translateY(-2px) scale(1.03);
    }
    
    .conversation-active div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"]):hover::before {
        opacity: 1;
        background: linear-gradient(135deg, rgba(232, 30, 70, 1) 0%, rgba(155, 35, 175, 1) 100%);
    }
    
    /* Layout horizontal do card */
    section[data-testid="stSidebar"] div[data-testid="stHorizontalBlock"]:has(button[key^="card_"]) {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        padding: 0 !important;
        margin: 0 !important;
        gap: 0 !important;
        height: 100% !important;
    }
    
    /* Ajustes para as colunas do card */
    section[data-testid="stSidebar"] div[data-testid="stHorizontalBlock"]:has(button[key^="card_"]) [data-testid="column"] {
        padding: 0 !important;
        height: 100% !important;
    }
    
    /* Botão principal de título */
    section[data-testid="stSidebar"] button[key^="card_"] {
        background: transparent !important;
        color: rgba(109, 29, 122, 0.85) !important;
        font-weight: 500 !important;
        text-align: left !important;
        border: none !important;
        border-radius: 0 !important;
        margin: 0 !important;
        box-shadow: none !important;
        padding: 0 0.7rem !important; /* Reduzido de 0.8rem */
        height: 29px !important; /* Reduzido de 32px */
        line-height: 29px !important; /* Reduzido de 32px */
        transition: all 0.3s ease;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        font-size: 0.81rem !important; /* Reduzido de 0.9rem */
        display: block !important;
        width: 100% !important;
        position: relative !important;
    }
    
    /* Classe específica para truncamento de texto */
    .truncate-text {
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        max-width: 100% !important;
    }
    
    /* Span para o título com truncamento */
    .conversation-title {
        max-width: calc(100% - 58px) !important; /* Reduzido de 65px */
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        display: inline-block !important;
    }
    
    /* Título da conversa ativa com gradiente da marca */
    .conversation-active button[key^="card_"] {
        background: linear-gradient(135deg, var(--marca-purple) 0%, var(--marca-red) 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 600 !important;
        position: relative;
        font-size: 0.9rem !important;
    }
    
    /* Estilos para badges de data */
    section[data-testid="stSidebar"] button[key^="card_"] .conversation-date-badge,
    .conversation-date-badge {
        position: absolute !important;
        right: 8px !important;
        font-size: 0.65rem !important;
        color: white !important;
        background: linear-gradient(135deg, var(--marca-purple) 0%, var(--marca-red) 100%) !important;
        border-radius: 6px !important;
        padding: 1px 4px !important;
        font-weight: 500 !important;
        opacity: 0.9 !important;
        line-height: 1.2 !important;
        display: inline-block !important;
        max-width: 50px !important;
        z-index: 2 !important;
    }
    
    /* Styling especial para o badge de data no card ativo */
    .conversation-active .conversation-date-badge {
        background: white !important;
        color: transparent !important;
        background-clip: text !important;
        -webkit-background-clip: text !important;
        background-image: linear-gradient(135deg, var(--marca-purple) 0%, var(--marca-red) 100%) !important;
        box-shadow: 0 1px 3px rgba(255, 255, 255, 0.3) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
    }
    
    /* Botões de ação pequenos e redondos com cores da marca */
    section[data-testid="stSidebar"] button[key^="edit_"],
    section[data-testid="stSidebar"] button[key^="delete_"] {
        background: linear-gradient(135deg, rgba(109, 29, 122, 0.12) 0%, rgba(204, 10, 43, 0.12) 100%) !important;
        border: 1px solid rgba(109, 29, 122, 0.3) !important;
        color: rgba(109, 29, 122, 0.8) !important;
        font-size: 0.72rem !important; /* Reduzido de 0.8rem */
        padding: 0 !important;
        min-height: 0 !important;
        height: 29px !important; /* Reduzido de 32px */
        width: 29px !important; /* Reduzido de 32px */
        margin: 0 !important;
        box-shadow: 0 2px 4px rgba(109, 29, 122, 0.15) !important; /* Reduzido de 5px para 4px */
        transition: all 0.2s ease;
        border-radius: 50% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        opacity: 0.95;
        position: relative !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
    }
    
    /* Mostrar botões claramente ao passar o mouse */
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"]):hover button[key^="edit_"],
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"]):hover button[key^="delete_"] {
        opacity: 1;
        transform: translateY(-50%) scale(1.08) !important; /* Reduzido de 1.1 */
    }
    
    /* Estilização do botão de editar com cores da marca */
    section[data-testid="stSidebar"] button[key^="edit_"] {
        background: linear-gradient(135deg, rgba(109, 29, 122, 0.15) 0%, rgba(204, 10, 43, 0.1) 100%) !important;
        margin-right: 5px !important; /* Reduzido de 6px */
    }
    
    section[data-testid="stSidebar"] button[key^="edit_"]:hover {
        background: linear-gradient(135deg, rgba(109, 29, 122, 0.3) 0%, rgba(204, 10, 43, 0.2) 100%) !important;
        border-color: var(--marca-purple) !important;
        color: var(--marca-purple) !important;
        box-shadow: 0 3px 7px rgba(109, 29, 122, 0.2) !important; /* Reduzido de 8px para 7px */
        transform: translateY(-50%) scale(1.08) !important; /* Reduzido de 1.1 */
    }
    
    /* Estilização do botão de excluir com cores da marca */
    section[data-testid="stSidebar"] button[key^="delete_"] {
        background: linear-gradient(135deg, rgba(204, 10, 43, 0.15) 0%, rgba(109, 29, 122, 0.1) 100%) !important;
        margin-right: 9px !important; /* Reduzido de 10px */
    }
    
    section[data-testid="stSidebar"] button[key^="delete_"]:hover {
        background: linear-gradient(135deg, rgba(204, 10, 43, 0.3) 0%, rgba(109, 29, 122, 0.2) 100%) !important;
        border-color: var(--marca-red) !important;
        color: var(--marca-red) !important;
        box-shadow: 0 3px 7px rgba(204, 10, 43, 0.2) !important; /* Reduzido de 8px para 7px */
        transform: translateY(-50%) scale(1.08) !important; /* Reduzido de 1.1 */
    }
    
    /* Container para os campos de edição */
    .rename-input {
        background: linear-gradient(135deg, rgba(109, 29, 122, 0.15) 0%, rgba(204, 10, 43, 0.15) 100%);
        padding: 0.9rem; /* Reduzido de 1rem */
        border-radius: 10px; /* Reduzido de 12px */
        margin-top: 0.6rem; /* Reduzido de 0.7rem */
        margin-bottom: 0.6rem; /* Reduzido de 0.7rem */
        box-shadow: 0 4px 10px rgba(109, 29, 122, 0.15); /* Reduzido de 12px para 10px */
        border: 1px solid rgba(109, 29, 122, 0.2);
    }
    
    /* Estilizar campo de texto para renomeação */
    [data-testid="stTextInput"] input {
        border-color: rgba(109, 29, 122, 0.3) !important;
        transition: all 0.3s ease;
        background-color: white !important;
    }
    
    [data-testid="stTextInput"] input:focus {
        border-color: var(--marca-purple) !important;
        box-shadow: 0 0 0 2px rgba(109, 29, 122, 0.2) !important;
    }
    
    /* Botões na janela de renomeação */
    button[key^="save_rename_"] {
        background: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 500 !important;
    }
    
    button[key^="cancel_rename_"] {
        background: rgba(0, 0, 0, 0.05) !important;
        color: #666 !important;
        border: 1px solid rgba(0, 0, 0, 0.1) !important;
    }
    
    /* Estilizar o diálogo de confirmação de exclusão */
    [data-testid="stAlert"] {
        border-left-color: var(--marca-red) !important;
        background-color: rgba(252, 233, 236, 0.7) !important;
        border-radius: 7px !important; /* Reduzido de 8px */
        margin: 0.6rem 0 !important; /* Reduzido de 0.7rem */
    }
    
    /* Botões de confirmação de exclusão */
    button[key^="confirm_delete_yes_"] {
        background: linear-gradient(135deg, #f5576c 0%, #d5267b 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 500 !important;
    }
    
    button[key^="confirm_delete_no_"] {
        background: rgba(0, 0, 0, 0.05) !important;
        color: #666 !important;
        border: 1px solid rgba(0, 0, 0, 0.1) !important;
    }
    
    /* Customização do cabeçalho da sidebar */
    .sidebar-header {
        background: linear-gradient(135deg, rgba(109, 29, 122, 0.12) 0%, rgba(204, 10, 43, 0.12) 100%);
        padding: 0.9rem 0.7rem; /* Reduzido de 1rem 0.8rem */
        margin-bottom: 1.1rem; /* Reduzido de 1.2rem */
        border-radius: var(--radius-md);
        position: relative;
        border-bottom: 1px solid rgba(109, 29, 122, 0.15);
    }
    
    /* Linha decorativa superior no cabeçalho da sidebar */
    .sidebar-header::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px; /* Era 3px, mantive pois é um valor mínimo */
        background: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%);
        border-radius: var(--radius-md) var(--radius-md) 0 0;
    }
    
    .sidebar-header h2 {
        color: var(--marca-purple);
        font-size: 1.08rem; /* Reduzido de 1.2rem */
        font-weight: 600;
        margin: 0;
    }
    
    /* Estilos para o menu contextual em mobile */
    .context-menu {
        position: absolute;
        top: 0;
        right: 0;
        background: white;
        border-radius: 7px; /* Reduzido de 8px */
        border: 1px solid rgba(109, 29, 122, 0.2);
        box-shadow: 0 4px 13px rgba(109, 29, 122, 0.15); /* Reduzido de 15px para 13px */
        z-index: 100;
        padding: 0.45rem; /* Reduzido de 0.5rem */
        display: none;
    }
    
    .context-menu.active {
        display: block;
    }
    
    .context-menu-item {
        padding: 0.45rem 0.7rem; /* Reduzido de 0.5rem 0.8rem */
        display: flex;
        align-items: center;
        gap: 7px; /* Reduzido de 8px */
        color: #333;
        font-size: 0.77rem; /* Reduzido de 0.85rem */
        border-radius: 4px;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .context-menu-item:hover {
        background: rgba(248, 240, 255, 0.8);
    }
    
    .context-menu-item.delete:hover {
        background: rgba(252, 233, 236, 0.8);
        color: var(--marca-red);
    }
    
    /* Acessibilidade - focus visível */
    section[data-testid="stSidebar"] button:focus-visible {
        outline: 2px solid var(--marca-purple) !important;
        outline-offset: 2px !important;
    }
    
    /* Tratamento para mobile e tablets */
    @media (max-width: 767px) {
        section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:has(button[key^="card_"]) {
            height: auto !important;
            max-height: none !important;
            padding: 0.27rem !important; /* Reduzido de 0.3rem */
        }
        
        section[data-testid="stSidebar"] button[key^="card_"] {
            padding: 0.54rem !important; /* Reduzido de 0.6rem */
            width: 100% !important;
            height: auto !important;
        }
        
        /* Botão de menu contextual para mobile */
        .mobile-menu-trigger {
            position: absolute;
            right: 7px; /* Reduzido de 8px */
            top: 50%;
            transform: translateY(-50%);
            width: 25px; /* Reduzido de 28px */
            height: 25px; /* Reduzido de 28px */
            display: flex;
            align-items: center;
            justify-content: center;
            background: transparent;
            border: none;
            color: rgba(109, 29, 122, 0.7);
            z-index: 10;
        }
    }
    """ 