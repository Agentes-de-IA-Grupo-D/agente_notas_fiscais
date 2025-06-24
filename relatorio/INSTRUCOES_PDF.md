# Instruções para Gerar o PDF do Relatório Final

## Opção 1: Usando o Script Python (Recomendado)

### 1. Instalar dependências
```bash
pip install markdown2 weasyprint
```

### 2. Executar o script
```bash
python gerar_pdf.py
```

### 3. Resultado
O arquivo `Grupo_D_Relatorio_Final.pdf` será gerado na pasta atual.

---

## Opção 2: Usando Pandoc (Alternativa)

### 1. Instalar Pandoc
- **Windows**: Baixar de https://pandoc.org/installing.html
- **macOS**: `brew install pandoc`
- **Linux**: `sudo apt-get install pandoc`

### 2. Gerar PDF
```bash
pandoc Grupo_D_Relatorio_Final.md -o Grupo_D_Relatorio_Final.pdf
```

---

## Opção 3: Conversão Online

### 1. Acessar conversor online
- https://www.markdowntopdf.com/
- https://md-to-pdf.fly.dev/

### 2. Fazer upload do arquivo
- Fazer upload do arquivo `Grupo_D_Relatorio_Final.md`
- Baixar o PDF gerado

---

## Opção 4: Usando VSCode

### 1. Instalar extensão
- Instalar a extensão "Markdown PDF" no VSCode

### 2. Gerar PDF
- Abrir o arquivo `Grupo_D_Relatorio_Final.md`
- Pressionar `Ctrl+Shift+P` (ou `Cmd+Shift+P` no macOS)
- Digitar "Markdown PDF: Export (pdf)"
- Selecionar a opção

---

## Estrutura dos Arquivos

```
agente_notas_fiscais/
├── Grupo_D_Relatorio_Final.md     # Relatório em Markdown
├── gerar_pdf.py                   # Script para gerar PDF
├── INSTRUCOES_PDF.md              # Este arquivo
├── main.py                        # Aplicação principal
├── agente/
│   └── agente_csv.py              # Agente de processamento
├── dados/
│   ├── 202401_NFs_Cabecalho.csv   # Dados de cabeçalho
│   └── 202401_NFs_Itens.csv       # Dados de itens
└── requirements.txt               # Dependências do projeto
```

---

## Conteúdo do Relatório

O relatório final inclui:

1. **Framework Escolhida**: LangChain + Streamlit + Groq API
2. **Estrutura da Solução**: Arquitetura e componentes
3. **4 Perguntas e Respostas**: FAQ sobre funcionalidades
4. **Link para Repositório**: GitHub e aplicação online
5. **Segurança**: Proteção de credenciais
6. **Análise dos Dados**: Estrutura e tipos de operações
7. **Funcionalidades**: Recursos implementados
8. **Limitações**: Pontos de melhoria
9. **Conclusão**: Impacto e contribuições

---

## Problemas Comuns

### Erro de dependências
```bash
pip install --upgrade pip
pip install markdown2 weasyprint
```

### Erro de encoding
- Verificar se o arquivo está salvo em UTF-8
- Usar editor que suporte UTF-8

### Erro de permissão
- Executar como administrador (Windows)
- Verificar permissões de escrita na pasta

---

## Formato Final

O PDF gerado terá:
- **Capa**: Título, curso, data
- **Índice**: Seções numeradas
- **Conteúdo**: 9 seções principais
- **Formatação**: Profissional e legível
- **Tamanho**: Aproximadamente 15-20 páginas

---
**Nota**: O arquivo PDF final deve ser nomeado como `Grupo_D_Relatorio_Final.pdf` conforme especificado no desafio.