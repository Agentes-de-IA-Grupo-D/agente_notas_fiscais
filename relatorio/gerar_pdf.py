#!/usr/bin/env python3
"""
Script para gerar o relatório final em PDF
Requer: pip install markdown2 weasyprint
"""

import markdown2
import weasyprint
from pathlib import Path

def gerar_pdf():
    """Converte o relatório markdown para PDF"""
    
    # Ler o arquivo markdown
    with open('Grupo_D_Relatorio_Final.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Converter markdown para HTML
    html_content = markdown2.markdown(
        markdown_content,
        extras=['tables', 'fenced-code-blocks', 'code-friendly']
    )
    
    # Adicionar CSS para formatação
    css_styles = """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 2cm;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            color: #34495e;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 5px;
        }
        h3 {
            color: #7f8c8d;
        }
        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        blockquote {
            border-left: 4px solid #3498db;
            margin: 0;
            padding-left: 20px;
            color: #7f8c8d;
        }
        .highlight {
            background-color: #fff3cd;
            padding: 10px;
            border-radius: 5px;
            border-left: 4px solid #ffc107;
        }
    </style>
    """
    
    # HTML completo
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Grupo D - Relatório Final: Agente de Notas Fiscais</title>
        {css_styles}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Gerar PDF
    weasyprint.HTML(string=full_html).write_pdf('Grupo_D_Relatorio_Final.pdf')
    
    print("✅ Relatório PDF gerado com sucesso: Grupo_D_Relatorio_Final.pdf")

if __name__ == "__main__":
    try:
        gerar_pdf()
    except ImportError:
        print("❌ Erro: Instale as dependências necessárias:")
        print("pip install markdown2 weasyprint")
    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")