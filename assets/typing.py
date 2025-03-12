def get_typing_css():
    return """
    /* Animação do cursor digitando */
    .typing-cursor {
        display: inline-block;
        width: 8px;
        height: 18px;
        background-color: var(--marca-purple);
        margin-left: 2px;
        animation: blink 1s infinite;
        vertical-align: middle;
        border-radius: 1px;
    }
    
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }
    """ 