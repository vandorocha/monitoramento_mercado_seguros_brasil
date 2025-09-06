import os
import pandas as pd

RAW_PATH = os.path.join(os.path.dirname(__file__), '../../data/raw')
PROCESSED_PATH = os.path.join(os.path.dirname(__file__), '../../data/processed')

os.makedirs(PROCESSED_PATH, exist_ok=True)

arquivos = ['ses_cias.csv', 'ses_ramos.csv', 'ses_seguros.csv']

for arquivo in arquivos:
    caminho = os.path.join(RAW_PATH, arquivo)
    if os.path.exists(caminho):
        print(f"Processando: {arquivo}")
        try:
            # Lê CSV com separador ; e codificação latin1
            df = pd.read_csv(
                caminho,
                sep=';',
                encoding='latin1',
                quotechar='"',
                on_bad_lines='warn'
            )

            # Remove espaços extras em todas as colunas string
            for col in df.select_dtypes(include='object').columns:
                df[col] = df[col].str.strip()

            # Converte colunas numéricas com vírgula para float
            for col in df.columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].str.replace(',', '.')
                    try:
                        df[col] = pd.to_numeric(df[col], errors='ignore')
                    except:
                        pass

            # Salva CSV limpo em processed
            caminho_saida = os.path.join(PROCESSED_PATH, arquivo)
            df.to_csv(caminho_saida, index=False, sep=';')
            print(f" - Salvo em: {caminho_saida}")
            print(f" - Linhas: {len(df)}, Colunas: {len(df.columns)}")

        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")
    else:
        print(f"Arquivo não encontrado: {arquivo}")
