# Grupo D - Proposta de Projeto: Desafio 3

- **Curso:** Agentes Autônomos com Redes Generativas - I2A2 Academy
- **Data:** Junho 2025
- **Versão:** 1.0

---

## 1. Nome do Grupo

Grupo D

## 2. Integrantes do Grupo

- Thalissa Kezia
- Joney Sousa
---

## 3. Descrição do Tema Escolhido

Desenvolvimento de um agente inteligente para análise de dados de notas fiscais, utilizando IA generativa e integração com frameworks modernos.

## 4. Público Alvo

Empresas, contadores, analistas fiscais e profissionais que necessitam de automação e inteligência na análise de grandes volumes de notas fiscais eletrônicas.

## 5. Justificativa do Tema Escolhido

A automação da análise de notas fiscais reduz erros, aumenta a produtividade e permite insights estratégicos para tomada de decisão. O uso de IA generativa potencializa a extração de valor dos dados fiscais.

## 6. Proposta de Desenvolvimento

O projeto será desenvolvido utilizando:
- **LangChain** para orquestração de agentes de IA
- **Streamlit** para interface web
- **Groq API** (Llama-4-Scout-17B) para processamento de linguagem natural
- **Pandas** para manipulação de dados
- **Arquivos CSV** como fonte de dados

### Arquitetura Resumida

```
Interface (Streamlit) → Processamento (LangChain) → Dados (CSV)
```

### Funcionalidades
- Upload múltiplo de arquivos CSV
- Perguntas em linguagem natural
- Análises estatísticas automáticas
- Tratamento robusto de erros
- Interface intuitiva
- Segurança de dados

## 7. Elementos Adicionais

### Exemplo de Tabela

| Mês/Ano   | NFs Processadas | Itens Detalhados |
|-----------|-----------------|------------------|
| 01/2024   | 102             | 567              |

### Exemplo de Gráfico (Sugestão)

Distribuição de operações por tipo (vendas, remessas, retornos, bonificações).

### Exemplo de Diagrama

```
Usuário → [Upload CSV] → [Agente IA] → [Resposta/Análise]
```

---

## 8. Links

- Aplicação: https://agentedecsv.streamlit.app
- Repositório: https://github.com/grupo-d/agente_notas_fiscais

---

## 9. Atualizações do Projeto

- Interface aprimorada
- Novas análises implementadas
- Documentação expandida
- Preparação para apresentação à banca

---

## 10. Status

- Concluído
- Pronto para apresentação.