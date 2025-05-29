import pandas as pd
import os

# Caminho absoluto para o arquivo
arquivo = r'C:\Users\diogo\Desktop\Projeto-2\dados\basecompleta.csv'

# Carregar o arquivo CSV
df = pd.read_csv(arquivo, sep=';', encoding='utf-8')

# Lista de colunas a remover
colunas_para_remover = [
    'Gestor',
    'Data Resposta',
    'Data Análise',
    'Data Recusa',
    'Data Finalização',
    'Prazo Analise Gestor',
    'Tempo Resposta',
    'Prazo Resposta',
    'Nome Fantasia',
    'UF',
    'Cidade',
    'Região',
    'Nota do Consumidor',
    'Avaliação Reclamação',
    'Procurou Empresa',
    'Respondida',
    'Situação',
    'Análise da Recusa'
]

# Remover colunas
df = df.drop(columns=colunas_para_remover, errors='ignore')

# Verifica quantos valores ausentes há por coluna
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Remove linhas que tiverem todos os campos vazios (caso existam)
df.dropna(how='all', inplace=True)

# Remove linhas onde os campos principais estão vazios (exemplo: 'Problema', 'Assunto' ou 'Área')
df.dropna(subset=['Problema', 'Assunto', 'Área'], inplace=True)

# Exibe novamente as 5 primeiras linhas
print("\nPrévia após remoção de ausentes:")
print(df.head())

# Exibir colunas restantes para confirmar
print("\nColunas restantes após limpeza:")
print(df.columns)

# Mostrar as primeiras linhas do DataFrame
print("\nPrimeiras linhas do DataFrame após limpeza:")
print(df.head())

# Padroniza colunas de texto: lowercase e strip()
colunas_texto = ['Canal de Origem', 'Sexo', 'Faixa Etária', 'Segmento de Mercado',
                 'Área', 'Assunto', 'Grupo Problema', 'Problema', 'Como Comprou Contratou']

for col in colunas_texto:
    df[col] = df[col].astype(str).str.lower().str.strip()

print("\nPadronização de textos concluída.")
print(df[colunas_texto].head())

# Verifica se a pasta 'dado_tratado' existe, e se não, cria a pasta
if not os.path.exists("dado_tratado"):
    os.makedirs("dado_tratado")

# Salva o DataFrame limpo e padronizado na nova pasta 'dado_tratado'
df.to_csv("dado_tratado/reclamacoes_tratadas.csv", index=False, encoding='utf-8-sig')
print("\nArquivo salvo em: dado_tratado/reclamacoes_tratadas.csv")
