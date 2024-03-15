import streamlit as st
import pandas as pd

# Carrega os dados do arquivo CSV
@st.cache_data
def load_data(filename):
    # Substitua o caminho abaixo pelo caminho do seu arquivo CSV
    df = pd.read_csv(filename)
    return df

# Verifica se os dados foram carregados na session state
if "data" not in st.session_state:
    st.error("Os dados ainda não foram carregados. Por favor, execute o arquivo home.py primeiro.")
    st.stop()


# Adiciona a imagem abaixo do menu na barra lateral
st.sidebar.image("logo.png", use_column_width=True)


# Carrega os dados do session state
df_data = st.session_state["data"]

# Carregar o arquivo "oldranking.csv"
filename_old = "datasets/oldranking.csv"  # Substitua pelo nome do seu arquivo
df_data_old = load_data(filename_old)

# Verificar se os dados foram carregados corretamente
if df_data_old.empty:
    st.error("Os dados da tabela antiga não puderam ser carregados. Verifique o caminho do arquivo.")
    st.stop()

# Mesclar os dataframes com base no nome de usuário
df_merged = pd.merge(df_data_old, df_data, on="Nick", suffixes=('_Antigo', '_Novo'), how="inner")

# Calcular a diferença de poder
df_merged['Diferença de Poder'] = df_merged['Poder_Novo'] - df_merged['Poder_Antigo']

# Exibir apenas as colunas desejadas
columns_to_display = ["Nick", "Poder_Antigo", "Poder_Novo", "Diferença de Poder"]
st.write(df_merged[columns_to_display])

st.write("""
Comparativo dos dias 13/03 e 15/03
""")
