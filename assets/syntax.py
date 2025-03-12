def get_syntax_css():
    return """
/* ======== ESTILOS PARA SINTAXE DE CÓDIGO ======== */
/* Estilo base para todos os blocos de código */
pre {
    background-color: #1e1e1e;
    border-radius: 10px;
    margin: 1rem 0;
    padding: 1rem;
    overflow-x: auto;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    position: relative;
}

pre::before {
    content: "código";
    position: absolute;
    top: 0;
    right: 0;
    background: linear-gradient(135deg, var(--marca-purple) 0%, var(--marca-red) 100%);
    color: white;
    font-size: 0.7rem;
    padding: 0.2rem 0.5rem;
    border-radius: 0 8px 0 8px;
    opacity: 0.8;
    text-transform: uppercase;
    font-weight: 600;
    letter-spacing: 0.5px;
}

pre code {
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    font-size: 0.85rem;
    line-height: 1.5;
    display: block;
    color: #d4d4d4;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

/* Elementos inline de código */
p code, li code, h1 code, h2 code, h3 code, h4 code {
    background-color: rgba(109, 29, 122, 0.1);
    color: var(--marca-purple);
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    font-size: 0.85em;
    white-space: nowrap;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(109, 29, 122, 0.1);
}

/* Cores para sintaxe */
.hljs-keyword {
    color: #569cd6;
    font-weight: bold;
}

.hljs-built_in {
    color: #4ec9b0;
}

.hljs-type {
    color: #4ec9b0;
}

.hljs-literal {
    color: #569cd6;
}

.hljs-number {
    color: #b5cea8;
}

.hljs-regexp {
    color: #d16969;
}

.hljs-string {
    color: #ce9178;
}

.hljs-subst {
    color: #d4d4d4;
}

.hljs-symbol {
    color: #d4d4d4;
}

.hljs-class {
    color: #4ec9b0;
}

.hljs-function {
    color: #dcdcaa;
}

.hljs-title {
    color: #dcdcaa;
}

.hljs-params {
    color: #d4d4d4;
}

.hljs-comment {
    color: #6a9955;
    font-style: italic;
}

.hljs-doctag {
    color: #608b4e;
}

.hljs-meta {
    color: #9b9b9b;
}

.hljs-meta-keyword {
    color: #569cd6;
}

.hljs-meta-string {
    color: #ce9178;
}

.hljs-section {
    color: #dcdcaa;
}

.hljs-builtin-name {
    color: #4ec9b0;
}

.hljs-name {
    color: #569cd6;
}

.hljs-tag {
    color: #569cd6;
}

.hljs-attr {
    color: #9cdcfe;
}

.hljs-attribute {
    color: #9cdcfe;
}

.hljs-variable {
    color: #9cdcfe;
}

.hljs-bullet {
    color: #d4d4d4;
}

.hljs-code {
    color: #d4d4d4;
}

.hljs-emphasis {
    font-style: italic;
}

.hljs-strong {
    font-weight: bold;
}

.hljs-formula {
    color: #d4d4d4;
}

.hljs-link {
    color: #569cd6;
    text-decoration: underline;
}

.hljs-quote {
    color: #6a9955;
    font-style: italic;
}

.hljs-selector-class {
    color: #d7ba7d;
}

.hljs-selector-id {
    color: #d7ba7d;
}

.hljs-selector-tag {
    color: #569cd6;
}

.hljs-selector-attr {
    color: #9cdcfe;
}

.hljs-selector-pseudo {
    color: #d7ba7d;
}

.hljs-template-tag {
    color: #569cd6;
}

.hljs-template-variable {
    color: #9cdcfe;
}

.hljs-addition {
    background-color: rgba(155, 185, 85, 0.2);
    color: #b5cea8;
}

.hljs-deletion {
    background-color: rgba(255, 0, 0, 0.2);
    color: #ce9178;
}

/* Estilo especial para Python */
.language-python .hljs-keyword {
    color: #ff79c6;
}

.language-python .hljs-built_in {
    color: #8be9fd;
}

.language-python .hljs-string {
    color: #f1fa8c;
}

.language-python .hljs-comment {
    color: #6272a4;
}

.language-python .hljs-function {
    color: #50fa7b;
}

.language-python .hljs-class {
    color: #8be9fd;
}

/* Estilo especial para JavaScript */
.language-javascript .hljs-keyword {
    color: #ff79c6;
}

.language-javascript .hljs-string {
    color: #f1fa8c;
}

.language-javascript .hljs-comment {
    color: #6272a4;
}

.language-javascript .hljs-function {
    color: #50fa7b;
}

.language-javascript .hljs-variable {
    color: #bd93f9;
}

/* Controle de linha e números */
.line-numbers {
    counter-reset: line;
    position: relative;
    padding-left: 3.5em;
}

.line-numbers code {
    position: relative;
}

.line-numbers code::before {
    counter-increment: line;
    content: counter(line);
    position: absolute;
    left: -3em;
    width: 2.5em;
    color: #858585;
    text-align: right;
    padding-right: 0.5em;
    border-right: 1px solid #404040;
    user-select: none;
}

/* Ajustes responsivos para mobile */
@media (max-width: 768px) {
    pre {
        font-size: 0.8rem;
        padding: 0.8rem;
    }
    
    pre::before {
        font-size: 0.6rem;
        padding: 0.1rem 0.3rem;
    }
    
    .line-numbers {
        padding-left: 2.5em;
    }
    
    .line-numbers code::before {
        left: -2.5em;
        width: 2em;
    }
}
"""