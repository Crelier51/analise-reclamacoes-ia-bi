# 📊 Análise Inteligente de Reclamações com IA e BI

Projeto completo de análise de dados baseado em reclamações públicas do [Consumidor.gov.br](https://dados.consultaspublicas.com.br/), integrando ferramentas de **coleta automatizada**, **armazenamento em nuvem (AWS S3)**, **processamento com IA (LLM)** e visualização em **Power BI**.

---

## ✅ Etapas Concluídas

### 1. Coleta de Dados
- Fonte: [Consumidor.gov.br](https://dados.consultaspublicas.com.br/)
- Script: `coleta_dados.py`
- Status: ✅ Concluído

### 2. Armazenamento em Nuvem (AWS S3)
- Bucket: `teste-diogo-upload`
- Estrutura:
  - `reclamacoes/`: dados brutos e tratados
  - `resultados/`: análises geradas pela IA
- Status: ✅ Concluído

### 3. Processamento com LLM (Ollama via Zapper)
- Funções:
  - Análise de sentimentos
  - Geração de resumos
  - Identificação de padrões
- Script: Pipeline completo que lê, processa e grava no S3
- Arquivo gerado: `resultado_analise_incremental.csv`
- Status: ✅ Concluído

### 4. Integração com Power BI
- Conexão direta com o S3 (AWS)
- Visualizações desenvolvidas:
  - Tendência de reclamações por ano
  - Filtros por segmento de mercado
  - Tabela com análise de sentimentos da IA
- Arquivo: `grafico-BI.pbix`
- Status: ✅ Concluído

🔗 (Opcional) [Acesse o Dashboard Interativo](https://app.powerbi.com/...)  

---

## 📂 Estrutura dos Arquivos no Repositório

├── coleta_dados.py # Script de coleta automatizada
├── limpeza_transformacao.py # Limpeza e pré-processamento
├── gera_amostra.py # Subset para testes rápidos
├── resultado_analise_amostra.csv # Saída com amostra
├── resultado_analise_incremental.csv# Arquivo completo da IA
├── grafico-BI.pbix # Power BI visualizações
└── arquitetura-diagrama.png # Diagrama da solução


---

## 🧱 Arquitetura da Solução

![Arquitetura da Solução](arquitetura-diagrama.png)

---

## 🎯 Objetivo

Construir uma solução moderna de **análise de reclamações públicas**, combinando ciência de dados, cloud computing, BI e modelos de linguagem (LLM).

---

## 🧠 Análises com Inteligência Artificial

A IA foi utilizada para:
- Identificar o **sentimento** de cada reclamação  
- Detectar **padrões e tópicos recorrentes**  
- Gerar **resumos automáticos**  

---

## 🔧 Tecnologias Utilizadas

- **Python**  
- **AWS S3**  
- **Ollama (via API Zapper.to)**  
- **Power BI**  
- **Git/GitHub**  

---

## 📈 Próximos Passos (Aperfeiçoamento)

1. Refinar visualizações no Power BI  
2. Adicionar filtros por região, empresa, assunto  
3. Incluir tendência mensal e insights da IA  
4. Publicar dashboard no Power BI Service (opcional)  
5. Finalizar e apresentar o diagrama da arquitetura  

---

## 📎 Sobre

Este projeto faz parte de um **desafio técnico prático de entrevista** com prazo original de 14 dias. A entrega buscou aplicar conceitos reais de engenharia e análise de dados com IA.

---

## 📬 Contato

Diogo Crelier  
[LinkedIn](https://www.linkedin.com/in/seu-usuario) *(adicione seu link real)*
