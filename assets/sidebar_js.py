def get_sidebar_js():
    return """
    // Script simplificado para gerenciar cliques nas conversas
    document.addEventListener('click', function(e) {
        // Função de debug 
        function debugLog(message) {
            console.log("[Debug] " + message);
        }
        
        debugLog("Clique detectado");
        
        // Verificar se o clique foi em um botão de ação
        if (e.target.classList && e.target.classList.contains('action-btn')) {
            debugLog("Clique em botão de ação");
            
            // Evitar propagação do clique
            e.stopPropagation();
            
            // Processar a ação do botão
            const action = e.target.getAttribute('data-action');
            const convId = e.target.getAttribute('data-conv-id');
            
            debugLog(`Ação: ${action}, ID: ${convId}`);
            
            if (action && convId) {
                // Construir o ID do botão
                const buttonId = `${action}_${convId}`;
                debugLog(`Procurando botão: ${buttonId}`);
                
                // Encontrar e clicar no botão
                setTimeout(function() {
                    const button = document.querySelector(`button[key="${buttonId}"]`);
                    if (button) {
                        debugLog(`Botão encontrado, clicando`);
                        button.click();
                    } else {
                        debugLog(`Botão não encontrado!`);
                    }
                }, 50);
            }
            
            return;
        }
        
        // Verificar se o clique foi no container ou em um filho do container (exceto botões de ação)
        const container = e.target.closest('.conversation-container');
        if (container) {
            debugLog("Clique no container de conversa");
            
            const convId = container.getAttribute('data-conv-id');
            debugLog(`ID da conversa: ${convId}`);
            
            if (convId) {
                // Buscar o botão correspondente
                const buttonId = `load_${convId}`;
                debugLog(`Procurando botão load: ${buttonId}`);
                
                // Tentar encontrar e clicar no botão após um breve delay
                setTimeout(function() {
                    const loadButton = document.querySelector(`button[key="${buttonId}"]`);
                    if (loadButton) {
                        debugLog(`Botão load encontrado, clicando`);
                        loadButton.click();
                    } else {
                        debugLog(`Botão load não encontrado!`);
                        
                        // Listar todos os botões disponíveis para debug
                        const allButtons = document.querySelectorAll('button[key]');
                        debugLog(`Total de botões encontrados: ${allButtons.length}`);
                        allButtons.forEach(btn => {
                            debugLog(`Botão disponível: ${btn.getAttribute('key')}`);
                        });
                    }
                }, 50);
            }
        }
    });
    
    // Verificar botões disponíveis no carregamento
    setTimeout(function() {
        console.log("Verificando botões disponíveis na página:");
        const allButtons = document.querySelectorAll('button[key]');
        console.log(`Total de botões: ${allButtons.length}`);
        allButtons.forEach(btn => {
            console.log(`Botão: ${btn.getAttribute('key')}`);
        });
    }, 500);
    
    console.log("Sidebar JS carregado com sucesso!");
    """ 