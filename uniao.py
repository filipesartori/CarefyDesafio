import pandas as pd
import os

#DataFrames para salvar cada Ano
df_ano2020 = pd.DataFrame()
df_ano2021 = pd.DataFrame()
df_ano2022 = pd.DataFrame()

diretorio = 'Planilhas'

for filename in os.listdir(diretorio):
    if filename.startswith('DadosBO_') and filename.endswith('.xlsx'):
        # Extrai o ano do nome do arquivo
        ano = int(filename.split('_')[1].split('.')[0])

        # Le o arquivo XLSX para um DataFrame
        df = pd.read_excel(os.path.join(diretorio, filename))

        # Adiciona o DataFrame ao ano correspondente
        if ano == 2020:
            df_ano2020 = pd.concat([df_ano2020, df], ignore_index=True)
        elif ano == 2021:
            df_ano2021 = pd.concat([df_ano2021, df], ignore_index=True)
        elif ano == 2022:
            df_ano2022 = pd.concat([df_ano2022, df], ignore_index=True)

#Função que salva os arquivos em csv
df_ano2020.to_csv('DadosBO_2020.csv', index=False)
df_ano2021.to_csv('DadosBO_2021.csv', index=False)
df_ano2022.to_csv('DadosBO_2022.csv', index=False)
