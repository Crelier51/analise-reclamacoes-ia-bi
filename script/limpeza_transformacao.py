import pandas as pd
import os

# Caminho absoluto para o arquivo
arquivo = r'C:\Users\diogo\Desktop\Projeto-2\dados\basecompleta.csv'

# Carregar o arquivo CSV
df = pd.read_csv(arquivo, sep=';', encoding='utf-8')

# Lista atualizada de colunas a remover (preservamos região, empresa, satisfação, etc.)
colunas_para_remover = [
    'Gestor',
    'Data Resposta',
    'Data Análise',
    'Data Recusa',
    'Data Finalização',
    'Prazo Analise Gestor',
    'Tempo Resposta',
    'Prazo Resposta',
    'Avaliação Reclamação',
    'Análise da Recusa'
]

# Remove colunas desnecessárias
df = df.drop(columns=colunas_para_remover, errors='ignore')

# Remove linhas com todos os campos vazios ou sem dados principais
df.dropna(how='all', inplace=True)
df.dropna(subset=['Problema', 'Assunto', 'Área'], inplace=True)

# Padroniza colunas de texto: lowercase e strip()
colunas_texto = [
    'Nome Fantasia', 'UF', 'Cidade', 'Região',
    'Nota do Consumidor', 'Procurou Empresa', 'Respondida', 'Situação',
    'Canal de Origem', 'Sexo', 'Faixa Etária', 'Segmento de Mercado',
    'Área', 'Assunto', 'Grupo Problema', 'Problema', 'Como Comprou Contratou'
]

for col in colunas_texto:
    if col in df.columns:
        df[col] = df[col].astype(str).str.lower().str.strip()

# Renomear colunas para facilitar uso no BI (ex: tirar espaços e colocar nomes mais curtos)
df.rename(columns={
    'Nome Fantasia': 'empresa',
    'Região': 'regiao',
    'Nota do Consumidor': 'nota_consumidor',
    'Procurou Empresa': 'procurou_empresa',
    'Respondida': 'respondida',
    'Situação': 'situacao',
    'Segmento de Mercado': 'segmento_mercado',
    'Canal de Origem': 'canal_origem',
    'Faixa Etária': 'faixa_etaria',
    'Como Comprou Contratou': 'como_comprou',
    'Grupo Problema': 'grupo_problema'
}, inplace=True)

# Criar pasta se não existir
if not os.path.exists("dado_tratado"):
    os.makedirs("dado_tratado")

# Salvar
df.to_csv("dado_tratado/reclamacoes_tratadas.csv", index=False, encoding='utf-8-sig')
print("\nArquivo salvo em: dado_tratado/reclamacoes_tratadas.csv")
