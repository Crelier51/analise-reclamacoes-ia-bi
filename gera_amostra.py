import pandas as pd

df = pd.read_csv('resultado_analise_incremental.csv')

amostra = df.head(100)

amostra.to_csv('resultado_analise_amostra.csv', index=False)

print("Arquivo de amostra criado: resultado_analise_amostra.csv")
