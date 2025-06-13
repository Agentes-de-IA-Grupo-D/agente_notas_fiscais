# Agente de Notas Fiscais

Este robô responde perguntas sobre notas fiscais usando Python + LangChain.

[➡️ Acesse o app online](https://agentedecsv.streamlit.app)

## Sobre o projeto

Este projeto foi desenvolvido como parte da atividade do curso **Agentes Autônomos com Redes Generativas** (I2A2 Academy).

O objetivo é criar um agente capaz de responder perguntas sobre arquivos CSV de notas fiscais fornecidos pelo curso, utilizando frameworks de IA generativa.

## Objetivo da atividade

Permitir que o usuário faça perguntas como:
- Qual é o fornecedor que teve maior montante recebido?
- Qual item teve maior volume entregue (em quantidade)?
- Entre outras consultas sobre os dados das notas fiscais.

O agente carrega os arquivos CSV, interpreta a pergunta do usuário e retorna a resposta, realizando cálculos e buscas conforme necessário. Se não for possível responder, o agente explica o motivo de forma clara.

## Como usar

1. Faça upload do(s) arquivo(s) CSV fornecidos pelo curso.
2. Digite sua pergunta sobre os dados.
3. O agente irá analisar a planilha e responder, se possível.

## Tecnologias utilizadas

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Groq API](https://groq.com/)

## Sobre os dados

Os arquivos utilizados são:
- `202401_NFs_Cabecalho.csv`: Cabeçalho de 100 notas fiscais de janeiro/2024.
- `202401_NFs_Itens.csv`: Itens correspondentes dessas notas.

Ambos em formato CSV, conforme especificação do curso.

---

**Projeto desenvolvido para a atividade do curso Agentes Autônomos com Redes Generativas – I2A2 Academy.**

