import requests
import pandas as pd

# URL da base mais recente (abril/2025)
url = 'https://dados.mj.gov.br/dataset/0182f1bf-e73d-42b1-ae8c-fa94d9ce9451/resource/8f22bdc1-3044-46ee-9dd1-4ace84da28e4/download/basecompleta2025-04.csv'

# Nome do arquivo para salvar no ambiente temporário do Colab
file_name = 'basecompleta.csv'

print("🔄 Baixando o arquivo de reclamações públicas...")

try:
    response = requests.get(url)
    response.raise_for_status()  # Lança erro se houver falha

    with open(file_name, 'wb') as f:
        f.write(response.content)

    print(f"✅ Arquivo salvo como: {file_name}")

    # Carrega uma prévia para verificação
    try:
        df = pd.read_csv(file_name, sep=';', encoding='utf-8', on_bad_lines='skip')
        print("\n📊 Prévia dos dados:")
        print(df.head(5))
        print(f"\n🔢 Total de linhas: {len(df)} | Total de colunas: {len(df.columns)}")
    except Exception as e:
        print("⚠️ Erro ao carregar CSV:", e)

except requests.exceptions.RequestException as e:
    print("❌ Erro ao fazer o download:", e)
