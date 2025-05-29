import requests
import pandas as pd

# URL do arquivo CSV
url = 'https://dados.mj.gov.br/dataset/0182f1bf-e73d-42b1-ae8c-fa94d9ce9451/resource/8f22bdc1-3044-46ee-9dd1-4ace84da28e4/download/basecompleta2025-04.csv'

# Nome do arquivo para salvar
file_name = 'basecompleta2025-04.csv'

# Baixar o arquivo
print("Baixando arquivo...")
response = requests.get(url)

# Verificar se o download foi bem-sucedido
if response.status_code == 200:
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print("Arquivo baixado com sucesso!")

    # Processar o arquivo CSV
    try:
        print("Processando arquivo CSV...")
        # Usar o delimitador correto (ponto e vírgula)
        data = pd.read_csv(file_name, on_bad_lines='skip', delimiter=';')

        print("Arquivo CSV carregado com sucesso!")
        
        # Exibir as primeiras linhas do arquivo
        print(data.head())

    except Exception as e:
        print(f"Erro ao processar o arquivo CSV: {e}")
else:
    print(f"Erro ao baixar o arquivo. Status code: {response.status_code}")
