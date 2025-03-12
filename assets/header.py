def get_header_css():
    return """
    .chat-header {
        text-align: center;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid rgba(109, 29, 122, 0.1);
    }
    
    .chat-header h1 {
        font-weight: 700;
        font-size: 2.5rem;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    .chat-header p {
        color: var(--text-secondary);
        font-size: 1.1rem;
        max-width: 600px;
        margin: 0 auto;
    }
    """ 