# 📊 Análise Inteligente de Reclamações com IA e BI

Este é um projeto prático que propõe uma solução completa para análise de reclamações públicas, utilizando ferramentas modernas de Ciência de Dados, Inteligência Artificial (LLMs) e Business Intelligence (BI).

---

## 🚀 Objetivo

Extrair insights valiosos a partir de dados públicos do portal [Consumidor.gov.br](https://www.consumidor.gov.br), automatizando as etapas de:

- Coleta de dados  
- Tratamento e padronização  
- Análise com modelos de linguagem (LLMs)  
- Visualização em dashboard interativo (Power BI)

---

## 🧱 Estrutura do Projeto

projeto/
├── dados/ # Arquivos de entrada brutos
│   └── basecompleta.csv # Base original coletada do consumidor.gov.br
├── reclamacoes/ # Diretório principal dos scripts
│   └── script/
│       ├── coleta_dados.py # Script para download automatizado dos dados
│       ├── limpeza_transformacao.py # Script para limpeza e pré-processamento
│       └── analise_llm.py # Script que envia dados para análise com IA
├── resultados/ # Arquivos finais processados, prontos para o BI
│   └── reclamacoes_final_para_bi.csv
├── llama_env/ # Ambiente virtual Python (isolado)
└── README.md # Documentação do projeto

---

## ✅ Etapas Concluídas

### 1. Coleta dos Dados

- Fonte: Portal oficial [Consumidor.gov.br](https://www.consumidor.gov.br)  
- Download automatizado do CSV mais recente via script Python  
- Armazenamento local para inspeção e testes iniciais

### 2. Limpeza e Transformação

- Remoção de colunas irrelevantes  
- Padronização textual (minúsculas, remoção de espaços extras)  
- Tratamento de valores ausentes  
- Geração de arquivo `.csv` limpo contendo colunas essenciais:

descricao, como_comprou_contratou, procurou_empresa, regiao, uf, cidade, sexo, faixa_etaria, mes_abertura, nome_fantasia, segmento_mercado, assunto

### 3. Processamento com IA (LLM)

- Integração com a API da [Zapper.to](https://zapper.to) (baseada no Ollama) para análise de texto  

**Aplicações:**  
- Análise de sentimento  
- Resumo automático das reclamações  
- Identificação de padrões  

**Colunas geradas no CSV final:**

sentimento_llm, resumo_llm, padrao_identificado

### 4. Armazenamento em Nuvem (AWS S3)

- Upload do arquivo final para o bucket S3  
- Link público habilitado para leitura (utilizado no Power BI):  
🔗 [Acessar CSV público](https://teste-diogo-upload.s3.us-east-2.amazonaws.com/resultados/amostra_50_linhas_analise_bi.csv)

### 5. Visualização e Dashboard (Power BI)

- Conexão direta ao CSV público no S3 para atualização automática dos dados  
- Criação de gráficos e métricas interativas para análise exploratória e apresentação executiva

**Principais visualizações do dashboard:**

- 📍 Volume de reclamações por região, estado e cidade  
- 🏢 Empresas com maior número de reclamações  
- 💬 Temas mais frequentes (assuntos)  
- 😊 Análise de sentimentos por empresa e região  
- 📈 Tendência temporal de reclamações por mês  
- 🧠 Padrões recorrentes identificados por IA  
- ✅ Índice de solução e nível de satisfação  

🔗 **Acesso ao dashboard (Power BI):** [Coloque o link aqui, se for público]

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
