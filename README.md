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

## Arquitetura da Solução

![Arquitetura da Solução](imagem/imagens-arquitetura.png)

---

## 🧱 Estrutura do Projeto

projeto/  
├── dados/ # Arquivos de entrada brutos  
│   └── basecompleta.csv # Base original coletada do consumidor.gov.br  
├── reclamacoes/ # Diretório principal dos scripts  
│   └── script/  
│       ├── coleta_dados.py # Script para download automatizado dos dados  
│       ├── limpeza_transformacao.py # Script para limpeza e pré-processamento  
│       ├── analise_llm.py # Script que envia dados para análise com IA  
│       ├── dados_tratados/ # Dados limpos e normalizados  
│       ├── reclamacoes_bi.pbix # Dashboard Power BI (arquivo local)  
│       ├── requirements.txt # Dependências do projeto  
├── resultados/ # Arquivos finais processados, prontos para o BI  
│   └── resultado_analise_incremental.csv  
├── imagem/ # Imagem da arquitetura da solução  
│   └── imagens-arquitetura.png  
├── llama_env/ # Ambiente virtual Python (isolado, não versionado)  
├── .gitignore  
├── LICENSE  
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
- Normalização de nomes de colunas (sem acentos, lowercase, underscores)  
- Garantia das colunas obrigatórias:  
  - empresa, regiao, procurou_empresa, satisfacao, assunto, indice_solucao  

### 3. Processamento com IA (LLM)

- Integração com a API da [Zapper.to](https://zapper.to), baseada no Ollama, para análise de texto  

**Aplicações:**  
- Análise de sentimento  
- Resumo automático das reclamações  
- Identificação de padrões  

**Colunas geradas no CSV final:**  
- sentimento_llm  
- resumo_llm  
- padrao_identificado  

### 4. Armazenamento em Nuvem (AWS S3)

- Upload do arquivo final para o bucket S3:  
  - `s3://teste-diogo-upload/resultados/resultado_analise_incremental.csv`  

### 5. Visualização e Dashboard (Power BI)

- Dashboard criado no Power BI Desktop com base no arquivo `resultado_analise_incremental.csv` armazenado no S3.  
- O arquivo `.pbix` foi incluído no repositório e pode ser aberto localmente para exploração dos dados.

**Principais visualizações criadas no dashboard:**  

- 📍 Volume de reclamações por região, estado e cidade  
- 🏢 Empresas com maior número de reclamações  
- 💬 Temas mais frequentes (assuntos)  
- 😊 Análise de sentimentos por empresa e região  
- 📈 Tendência temporal de reclamações por mês  
- 🧠 Padrões recorrentes identificados por IA  
- ✅ Índice de solução e nível de satisfação  

> ⚠️ **Observação:** A publicação do dashboard no Power BI Service não foi concluída devido a problemas técnicos com o login da conta de estudante. O arquivo `.pbix` está disponível no repositório para avaliação local.

---

## 🗂️ Checklist Final de Entrega

- [x] Coleta de dados automatizada  
- [x] Armazenamento em nuvem (S3)  
- [x] Processamento com LLM (análise de sentimento, padrões, resumo)  
- [x] Dashboard criado no Power BI Desktop  
- [x] Arquivo `.pbix` incluso no repositório  
- [x] Arquitetura da solução documentada  
- [x] README completo e atualizado  
- [x] Controle de versão com commits no GitHub  

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Seu Nome**  
GitHub: [Seu GitHub](https://github.com/seuusuario)  

---
