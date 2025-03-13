# CHATSeek - Assistente Virtual Inteligente

![CHATSeek Logo](https://via.placeholder.com/150x150.png?text=CHATSeek)

CHATSeek é uma aplicação de chat assistente desenvolvida com Streamlit e integrada aos modelos de linguagem GPT da OpenAI. Com uma interface moderna e intuitiva, oferece uma experiência de conversação avançada com histórico persistente de conversas.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Arquitetura](#arquitetura)
- [Identidade Visual](#identidade-visual)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Execução](#instalação-e-execução)
- [Customização](#customização)
- [Desenvolvimento Futuro](#desenvolvimento-futuro)

## 🔍 Visão Geral

CHATSeek oferece uma interface amigável e poderosa para interagir com modelos de linguagem, mantendo um histórico de conversas organizado e facilmente acessível. A aplicação possui um design moderno e responsivo, seguindo uma identidade visual consistente.

![Screenshot da Aplicação](https://via.placeholder.com/800x450.png?text=CHATSeek+Interface)

## ✨ Funcionalidades

### Interface de Chat

- **Design Moderno**: Layout limpo e espaçoso para fácil leitura
- **Suporte a Markdown**: Formatação avançada nas respostas, incluindo:
  - Blocos de código com destacamento de sintaxe
  - Links clicáveis automaticamente formatados
  - Elementos tipográficos (negrito, itálico, etc.)
- **Feedback Visual**: Animação de digitação durante processamento de respostas
- **Controle de Interações**:
  - Botão para cancelar respostas em andamento
  - Tratamento de timeout para prevenir travamentos

### Sistema de Histórico de Conversas

- **Gerenciamento Completo**:
  - Armazenamento persistente de conversas em formato JSON
  - Geração automática de títulos descritivos
  - Organização cronológica (mais recentes primeiro)
  - Badges de data integrados nos cards de conversa
- **Operações de Gerenciamento**:
  - Criação de novas conversas
  - Renomeação de conversas existentes
  - Exclusão de conversas com confirmação de segurança
  - Navegação intuitiva entre diferentes conversas

### Integração com LLMs

- **Modelo GPT-4o-mini**: Processamento avançado de linguagem natural
- **Streaming de Respostas**: Visualização em tempo real da geração de texto
- **Histórico Contextual**: Manutenção de contexto entre mensagens da mesma conversa

## 🏗️ Arquitetura

A aplicação segue uma arquitetura modular e bem estruturada:

```
├── chat.py                    # Arquivo principal da aplicação
├── assets/                    # Componentes visuais e estilos
│   ├── apply_styles.py        # Utilitário para aplicação de estilos
│   ├── base.py                # Estilos base e variáveis CSS
│   ├── chat.py                # Estilos para a área de chat
│   ├── header.py              # Estilos para o cabeçalho
│   ├── sidebar.py             # Estilos para a barra lateral principal
│   ├── sidebar_extra.py       # Estilos adicionais da barra lateral
│   ├── sidebar_js.py          # Scripts JavaScript para a barra lateral
│   ├── syntax.py              # Estilos para destacamento de sintaxe
│   └── typing.py              # Animações de digitação
└── saved_conversations.json   # Banco de dados de conversas salvas
```

### Componentes Principais

#### 1. Classe `ChatApplication`
Gerencia a lógica de comunicação com os modelos de linguagem:
- Integração com OpenAI via LangChain
- Gestão de histórico de mensagens por sessão
- Tratamento de erros e fallbacks

#### 2. Classe `StreamlitInterface`
Responsável pela interface de usuário:
- Renderização de componentes visuais
- Gerenciamento de estados de sessão
- Implementação do sistema de histórico

#### 3. Sistema de Estilos Modular
Organiza a aplicação em componentes visuais independentes:
- CSS modular com variáveis para consistência visual
- Implementação responsiva para diferentes dispositivos
- Animações e transições para melhorar a experiência

## 🎨 Identidade Visual

A aplicação utiliza uma identidade visual consistente baseada nas seguintes cores e gradientes:

```css
--marca-red: #CC0A2B;
--marca-purple: #6D1D7A;
--gradient-primary: linear-gradient(135deg, var(--marca-red) 0%, var(--marca-purple) 100%);
--chat-user: linear-gradient(135deg, #FFE5E5 0%, #FFFAFA 100%);
--chat-assistant: linear-gradient(135deg, #F8F0FF 0%, #FCE9EC 100%);
--shadow-primary: 0 4px 6px -1px rgba(109, 29, 122, 0.1);
```

Estes elementos visuais são aplicados consistentemente em:
- Cabeçalho da aplicação
- Conversa ativa no histórico
- Botões e elementos interativos
- Badges e indicadores visuais

## 🔧 Tecnologias Utilizadas

### Frontend
- **Streamlit**: Framework principal para interface de usuário
- **HTML/CSS**: Personalização avançada de elementos
- **JavaScript**: Interatividade adicional para melhor experiência

### Backend
- **Python**: Linguagem principal da aplicação
- **LangChain**: Framework para integração com LLMs
- **OpenAI API**: Processamento avançado de linguagem natural

### Persistência de Dados
- **JSON**: Armazenamento de histórico de conversas
- **Session State**: Gerenciamento de estado temporário

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes Python)
- Chave API da OpenAI

### Instalação

1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/seu-usuario/chatseek.git
   cd chatseek
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure sua chave API em um arquivo `.env`:
   ```
   API_KEY=sua_chave_api_openai
   ```

### Execução

Execute a aplicação com o comando:
```bash
streamlit run chat.py
```

A aplicação estará disponível em `http://localhost:8501`.

## 🔄 Customização

A aplicação foi projetada para ser facilmente personalizável:

- **Identidade Visual**: Modifique as variáveis CSS em `assets/base.py`
- **Modelo de IA**: Altere o modelo na classe `ChatApplication`
- **Layout**: Ajuste os elementos visuais nos arquivos da pasta `assets/`

## 🔮 Desenvolvimento Futuro

Melhorias e expansões planejadas para a aplicação:

1. **Suporte a Múltiplos Modelos**: Integração com outros provedores de LLMs
2. **Processamento de Documentos**: Upload e análise de arquivos
3. **Exportação**: Opções para exportar conversas em diferentes formatos
4. **Orquestração Avançada**: Melhorar o fluxo de orquestração usando LangChain com LangGraph para criar fluxos de conversação mais complexos e eficientes
5. **Implementação de Ferramentas**: Adicionar suporte a ferramentas externas que o assistente possa utilizar (pesquisa web, análise de dados, visualizações, etc.)

## 🔨 Débitos Técnicos

Melhorias técnicas identificadas para implementação futura:

1. **Banco de Dados**: Migração do armazenamento atual em JSON para MongoDB, proporcionando melhor escalabilidade, consultas mais eficientes e suporte adequado para múltiplos usuários
2. **Refatoração da Arquitetura**: Separação mais clara entre camadas de apresentação, lógica de negócios e acesso a dados
3. **Testes Automatizados**: Implementação de testes unitários e de integração para garantir estabilidade em atualizações futuras

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

Desenvolvido com ❤️ usando Streamlit e OpenAI. 