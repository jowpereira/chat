def get_header_css():
    return """
    .chat-header {
        text-align: center;
        margin-bottom: 2.5rem;
        padding: 1.5rem 0 1.2rem;
        position: relative;
        border-bottom: 1px solid rgba(109, 29, 122, 0.15);
        background: var(--gradient-subtle);
        border-radius: 0 0 var(--radius-lg) var(--radius-lg);
        box-shadow: var(--shadow-sm);
    }
    
    /* Linha decorativa na parte superior do cabeçalho */
    .chat-header::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: var(--gradient-primary);
        z-index: 1;
    }
    
    .chat-header h1 {
        font-weight: 700;
        font-size: 2.5rem;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        margin-left: 45px;
        letter-spacing: -1px;
        text-shadow: 0 2px 10px rgba(109, 29, 122, 0.1);
        position: relative;
        display: inline-block;
    }
    
    /* Robozinho ao lado do título */
    .chat-header h1::before {
        content: "🤖";
        position: absolute;
        display: flex;
        align-items: center;
        justify-content: center;
        top: 50%;
        left: -57px;
        transform: translateY(-50%);
        width: 45px;
        height: 45px;
        margin-right: 12px;
        font-size: 24px;
        background: linear-gradient(145deg, rgba(109, 29, 122, 0.7) 0%, rgba(156, 46, 161, 0.6) 100%);
        border-radius: 50%;
        color: white !important;
        -webkit-text-fill-color: white !important;
        filter: drop-shadow(0 2px 3px rgba(109, 29, 122, 0.2));
        transition: transform 0.3s ease;
        border: 1.5px solid rgba(255, 255, 255, 0.9);
        z-index: 2;
        padding-bottom: 2px;
    }
    
    .chat-header h1:hover::before {
        transform: translateY(-50%) scale(1.1) rotate(5deg);
    }
    
    /* Efeito sutil no título */
    .chat-header h1::after {
        content: "";
        position: absolute;
        bottom: -5px;
        left: 50%;
        transform: translateX(-50%);
        width: 40px;
        height: 2px;
        background: var(--gradient-primary);
        border-radius: var(--radius-sm);
    }
    
    .chat-header p {
        color: var(--text-secondary);
        font-size: 1.1rem;
        max-width: 600px;
        margin: 1.2rem auto 0;
        line-height: 1.6;
        position: relative;
    }
    """ 