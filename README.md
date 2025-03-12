# CHATSeek - Estrutura de CSS e JavaScript

Este projeto utiliza uma estrutura modularizada para gerenciar CSS e JavaScript através de módulos Python que retornam strings.

## Estrutura da pasta `chat/assets`

A pasta `assets` contém módulos Python que retornam strings de CSS e JavaScript para diferentes partes da aplicação:

- **base.py**: Estilos base da aplicação, como variáveis CSS, reset global e estilos comuns
- **sidebar.py**: Estilos base da barra lateral
- **sidebar_extra.py**: Estilos adicionais para a barra lateral
- **sidebar_js.py**: JavaScript para interatividade da barra lateral
- **chat.py**: Estilos para o componente principal de chat
- **syntax.py**: Estilos para destaque de sintaxe de código
- **header.py**: Estilos para o cabeçalho da aplicação
- **typing.py**: Estilos para a animação do cursor de digitação
- **apply_styles.py**: JavaScript para garantir a aplicação correta dos estilos

## Como usar os módulos

Os módulos são importados no arquivo principal `chat/chat.py` e utilizados na função `_inject_custom_css()`:

```python
from assets import base, sidebar, chat, syntax
from assets import sidebar_js, sidebar_extra, apply_styles, header, typing

def _inject_custom_css(self):
    """Injeta todo o CSS modularizado"""
    css = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
                    
        {base.get_base_css()}
        {sidebar.get_sidebar_css()}
        {sidebar_extra.get_sidebar_extra_css()}
        {chat.get_chat_css()}
        {syntax.get_syntax_css()}
        {header.get_header_css()}
        {typing.get_typing_css()}
    </style>
    """
    
    # Garantir que as variáveis CSS sejam definidas
    st.markdown(css, unsafe_allow_html=True)
    
    # Garantir que o CSS seja aplicado imediatamente
    st.markdown(f"""
    <script>
        {apply_styles.get_apply_styles_js()}
    </script>
    """, unsafe_allow_html=True)
```

O JavaScript da barra lateral é injetado separadamente na função `render_sidebar()`:

```python
st.sidebar.markdown("""
<div class="sidebar-header">
    <h2>Conversas</h2>
</div>

<script>
    {sidebar_js.get_sidebar_js()}
</script>
""", unsafe_allow_html=True)
```

## Vantagens desta abordagem

1. **Modularidade**: Facilita a manutenção e organização do código
2. **Reutilização**: Componentes CSS podem ser reutilizados em diferentes partes da aplicação
3. **Manutenção**: Mudanças em um componente não afetam outros componentes
4. **Legibilidade**: Código mais limpo e organizado
5. **Escalabilidade**: Facilita adicionar novos estilos e componentes 