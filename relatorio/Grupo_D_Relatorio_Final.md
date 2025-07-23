# Grupo D - Relatório Final: Agente de Notas Fiscais

- Curso:** Agentes Autônomos com Redes Generativas - I2A2 Academy
- Data:** Junho 2025
- Versão:** 1.0

---

## 1. Framework Escolhida

### 1.1 Stack Tecnológica Principal

**LangChain + Streamlit + Groq API**

O projeto utiliza uma combinação de tecnologias modernas para criar um agente inteligente de análise de dados fiscais:

- **LangChain**: Framework principal para desenvolvimento de agentes de IA, permitindo integração com modelos de linguagem e ferramentas de processamento de dados
- **Streamlit**: Framework web para criação de interfaces de usuário intuitivas e responsivas
- **Groq API**: Provedor de IA com modelo Llama-4-Scout-17B para processamento de linguagem natural
- **Pandas**: Biblioteca para manipulação e análise de dados estruturados

### 1.2 Justificativa da Escolha

A escolha do LangChain como framework principal foi baseada em:

- **Flexibilidade**: Permite integração com múltiplos provedores de IA
- **Capacidade de RAG**: Suporte nativo para Retrieval-Augmented Generation
- **Ferramentas Integradas**: Agentes pandas para análise de dados
- **Comunidade Ativa**: Documentação extensa e suporte da comunidade
- **Escalabilidade**: Arquitetura modular que permite expansão futura

---

## 2. Como a Solução Foi Estruturada

### 2.1 Arquitetura do Sistema

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Interface     │    │   Processamento │    │   Armazenamento │
│   Streamlit     │◄──►│   LangChain     │◄──►│   CSV Files     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Upload de     │    │   Agente        │    │   Dados de      │
│   Arquivos      │    │   Pandas        │    │   Notas Fiscais │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 2.2 Componentes Principais

#### 2.2.1 Interface de Usuário (`main.py`)
- **Upload múltiplo de arquivos CSV**
- **Campo de entrada para perguntas em linguagem natural**
- **Exibição de respostas formatadas**
- **Tratamento de erros amigável**

#### 2.2.2 Agente de Processamento (`agente/agente_csv.py`)
- **Classe AgenteNotasFiscais**: Encapsula lógica de processamento
- **Integração com LangChain**: Criação de agentes pandas
- **Merge de dados**: Combinação de cabeçalho e itens das NFs

#### 2.2.3 Dados de Entrada
- **202401_NFs_Cabecalho.csv**: 102 registros com informações do cabeçalho
- **202401_NFs_Itens.csv**: 567 registros com detalhes dos itens

### 2.3 Fluxo de Processamento

1. **Upload**: Usuário faz upload dos arquivos CSV
2. **Carregamento**: Sistema carrega e valida os dados
3. **Contextualização**: Informações das colunas são adicionadas ao contexto
4. **Processamento**: Agente LangChain processa a pergunta
5. **Resposta**: Resultado é formatado e exibido ao usuário

---

## 3. Perguntas e Respostas

### 3.1 Qual é a capacidade de análise do agente de notas fiscais?

**Resposta:** O agente possui capacidade avançada de análise de dados através da integração entre LangChain e pandas. Ele pode processar arquivos CSV de notas fiscais contendo informações detalhadas como chave de acesso, dados do emitente e destinatário, valores, produtos/serviços, códigos NCM, CFOP, entre outros. O agente utiliza o modelo Llama-4-Scout-17B da Groq para interpretar perguntas em linguagem natural e gerar análises estatísticas, relatórios e insights sobre os dados fiscais.

### 3.2 Como o agente trata diferentes tipos de operações fiscais?

**Resposta:** O agente identifica e categoriza automaticamente diferentes tipos de operações fiscais presentes nos dados, incluindo vendas internas, operações interestaduais, remessas, retornos, bonificações e doações. Ele pode analisar padrões de CFOP (Código Fiscal de Operações e Prestações), natureza das operações, e identificar se são operações presenciais ou não presenciais. O sistema também diferencia entre consumidores finais e contribuintes normais, permitindo análises específicas por tipo de operação.

### 3.3 Quais são as funcionalidades de interface do usuário?

**Resposta:** O agente oferece uma interface web intuitiva desenvolvida com Streamlit, permitindo upload de múltiplos arquivos CSV simultaneamente. Os usuários podem fazer perguntas em linguagem natural sobre os dados carregados, e o sistema fornece respostas contextualizadas. A interface inclui tratamento de erros amigável, com mensagens específicas para diferentes tipos de problemas (limite de API, arquivos vazios, dados não encontrados). O sistema também oferece feedback visual sobre o status das operações e sugestões para melhorar as consultas.

### 3.4 Como o agente garante a segurança e confidencialidade dos dados fiscais?

**Resposta:** O agente implementa várias camadas de segurança: utiliza variáveis de ambiente (.env) para armazenar chaves de API de forma segura, evitando exposição de credenciais no código fonte. O sistema processa dados localmente sem armazenamento permanente, garantindo que informações sensíveis não sejam retidas. A interface web não exibe dados brutos sensíveis, apenas análises processadas. O código inclui validações para evitar execução de código perigoso e implementa tratamento de erros que não revela informações internas do sistema aos usuários finais.

---

## 4. Link para o Repositório

**GitHub Repository:** [https://github.com/grupo-d/agente_notas_fiscais](https://github.com/grupo-d/agente_notas_fiscais)

**Aplicação Online:** [https://agentedecsv.streamlit.app](https://agentedecsv.streamlit.app)

---

## 5. Segurança e Credenciais

### 5.1 Proteção de Chaves API

- **Variáveis de Ambiente**: Todas as chaves de API são armazenadas em arquivo `.env`
- **Gitignore**: Arquivo `.env` está incluído no `.gitignore` para evitar commit acidental
- **Validação**: Sistema verifica presença das credenciais antes da execução

### 5.2 Dados Sensíveis

- **Processamento Local**: Dados são processados localmente sem armazenamento
- **Anonimização**: Informações pessoais são mascaradas nos dados de exemplo
- **Logs Seguros**: Sistema não registra dados sensíveis em logs

---

## 6. Análise dos Dados

### 6.1 Estrutura dos Dados

**Cabeçalho das NFs (102 registros):**
- Chave de acesso, modelo, série, número
- Dados do emitente e destinatário
- Natureza da operação, valores, datas

**Itens das NFs (567 registros):**
- Produtos/serviços, códigos NCM
- Quantidades, valores unitários e totais
- CFOP e classificações fiscais

### 6.2 Tipos de Operações Identificadas

- **Vendas**: Internas e interestaduais
- **Remessas**: Para consignação, industrialização
- **Retornos**: De mercadorias e materiais
- **Bonificações**: Doações e brindes
- **Outras**: Entradas e saídas diversas

### 6.3 Principais Setores

- **Educação**: Livros e materiais didáticos
- **Saúde**: Produtos médicos e hospitalares
- **Tecnologia**: Equipamentos de informática
- **Alimentação**: Produtos alimentícios
- **Combustíveis**: Óleos e lubrificantes

---

## 7. Funcionalidades Implementadas

### 7.1 Análises Disponíveis

- **Consultas por valor**: Maior/menor valor, médias, totais
- **Análises por fornecedor**: Ranking de fornecedores
- **Filtros por período**: Consultas por data
- **Análises por produto**: Volume e valor por item
- **Operações por UF**: Distribuição geográfica

### 7.2 Tratamento de Erros

- **Rate Limiting**: Controle de requisições à API
- **Arquivos Inválidos**: Validação de formato CSV
- **Dados Vazios**: Tratamento de datasets incompletos
- **Perguntas Complexas**: Sugestões para reformulação

### 7.3 Interface Responsiva

- **Upload Drag & Drop**: Interface intuitiva para arquivos
- **Feedback Visual**: Indicadores de progresso
- **Histórico**: Manutenção de contexto entre perguntas
- **Exportação**: Possibilidade de exportar resultados

---

## 8. Limitações e Melhorias Futuras

### 8.1 Limitações Atuais

- **Dependência de API Externa**: Requer conexão com Groq
- **Processamento Síncrono**: Não suporta operações assíncronas
- **Limite de Tamanho**: Restrições no tamanho dos arquivos
- **Idioma**: Interface apenas em português

### 8.2 Melhorias Propostas

- **Cache Local**: Implementar cache para reduzir chamadas à API
- **Processamento Assíncrono**: Suporte a operações em background
- **Múltiplos Idiomas**: Interface multilíngue
- **Relatórios Avançados**: Gráficos e dashboards interativos
- **Integração com SEFAZ**: Conexão direta com sistemas fiscais

---

## 9. Conclusão

O Agente de Notas Fiscais desenvolvido pelo Grupo D demonstra o potencial da integração entre frameworks de IA generativa e ferramentas de análise de dados. A solução oferece uma interface intuitiva para análise de dados fiscais complexos, permitindo que usuários não técnicos obtenham insights valiosos através de perguntas em linguagem natural.

O projeto atende aos objetivos propostos pelo curso, demonstrando competência no uso de LangChain, integração com APIs de IA, e desenvolvimento de interfaces web responsivas. A arquitetura modular permite expansões futuras e a implementação de funcionalidades avançadas.

### 9.1 Impacto e Valor

- **Automatização**: Reduz tempo de análise manual de dados fiscais
- **Acessibilidade**: Democratiza acesso a análises complexas
- **Precisão**: Minimiza erros humanos em processamento de dados
- **Escalabilidade**: Suporta volumes crescentes de dados

### 9.2 Contribuições Técnicas

- **Integração LangChain-Groq**: Demonstração de arquitetura híbrida
- **Interface Streamlit**: Exemplo de UI moderna para análise de dados
- **Tratamento de Erros**: Padrões robustos para sistemas de IA
- **Segurança**: Boas práticas para proteção de dados sensíveis

---

**Desenvolvido por:** Grupo D - Agentes Autônomos com Redes Generativas
**Orientação:** I2A2 Academy
**Período:** Junho 2025

## Integrantes do Grupo

- Thalissa Kezia
- Joney Sousa
