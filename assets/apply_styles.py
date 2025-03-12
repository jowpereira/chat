def get_apply_styles_js():
    return """
    // Função para garantir que o CSS seja aplicado corretamente
    function applyCustomStyles() {
        const sidebarElement = document.querySelector('[data-testid="stSidebar"]');
        if (sidebarElement) {
            // Forçar repaint da sidebar
            sidebarElement.style.display = 'none';
            setTimeout(function() {
                sidebarElement.style.display = '';
            }, 10);
        }
    }
    
    // Executar assim que o DOM estiver pronto
    document.addEventListener('DOMContentLoaded', applyCustomStyles);
    
    // Como backup, tentar novamente após um curto intervalo
    setTimeout(applyCustomStyles, 500);
    """ 