# 📊 Análise Inteligente de Reclamações com IA e BI

Projeto prático com objetivo de construir uma solução completa de análise de reclamações públicas, utilizando ferramentas modernas de **ciência de dados**, **LLMs (Inteligência Artificial)** e **Business Intelligence (BI)**.

## 🚀 Objetivo

Extrair valor de dados públicos do portal [Consumidor.gov.br](https://www.consumidor.gov.br), automatizando o processo de coleta, tratamento, análise com IA e visualização em dashboard interativo.

---

## 🧱 Estrutura do Projeto
projeto/
├── dados/
│ └── basecompleta.csv
├── reclamacoes/
│ ├── script/
│ │ ├── coleta_dados.py
│ │ ├── limpeza_transformacao.py
│ │ └── analise_llm.py
├── resultados/
│ └── reclamacoes_final_para_bi.csv
├── llama_env/ (ambiente virtual)
└── README.md

---

## ✅ Etapas Concluídas

### 1. Coleta dos Dados
- Fonte: Portal oficial Consumidor.gov.br.
- Download automatizado do CSV mais recente via script.
- Armazenamento local para inspeção e testes.

### 2. Limpeza e Transformação
- Remoção de colunas irrelevantes.
- Padronização textual (minúsculas, espaços).
- Tratamento de valores ausentes.
- Geração de CSV limpo contendo:
  - `Descrição`, `Como comprou/contratou`, `Procurou a empresa?`, `Região`, `UF`, `Cidade`, `Sexo`, `Faixa Etária`, `Mês de abertura`, `Nome Fantasia`, `Segmento de mercado`, `Assunto`.

### 3. Processamento com IA (LLM)
- Uso da API **Zapper.to (Ollama)** para análise de texto.
- Aplicações:
  - **Análise de Sentimento**
  - **Resumo automático da reclamação**
  - **Identificação de padrões**
- Geração de CSV com colunas adicionais: `Sentimento`, `Resumo IA`, `Padrão Identificado`.

### 4. Armazenamento em Nuvem (AWS S3)
- Arquivo final enviado para:
s3://teste-diogo-upload/resultados/reclamacoes_final_para_bi.csv

- Link público habilitado para leitura via URL (usado no Power BI).

### 5. Visualização em Power BI
- Conexão direta via URL pública do CSV.
- Visualizações criadas:
- Volume de reclamações por **Região**, **Empresa**, **Assunto**.
- **Tendência temporal** (mês de abertura).
- **Satisfação** e **Índice de solução**.
- Resultados da IA (sentimento, padrão, resumo).

---

## 📂 Tecnologias Utilizadas

- **Python** (pandas, requests)
- **AWS S3** (armazenamento na nuvem)
- **Zapper.to / Ollama** (IA via LLMs)
- **Power BI** (visualização de dados)
- **Git/GitHub** (versionamento e documentação)

---

## 📌 Como Reproduzir o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/Crelier51/analise-reclamacoes-ia-bi.git
cd analise-reclamacoes-ia-bi
