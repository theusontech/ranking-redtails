import streamlit as st
import pandas as pd

# Carrega os dados do arquivo CSV
@st.cache
def load_data():
    # Substitua o caminho abaixo pelo caminho do seu arquivo CSV
    df = pd.read_csv("ranking.csv")
    return df

# Verifica se os dados foram carregados na session state
if "data" not in st.session_state:
    st.error("Os dados ainda não foram carregados. Por favor, execute o arquivo home.py primeiro.")
    st.stop()

# Carrega os dados do session state
df_data = st.session_state["data"]

# Verifica se a coluna "Classe" existe nos dados
if "Classe" not in df_data.columns:
    st.error("A coluna 'Classe' não foi encontrada nos dados. Por favor, verifique se os dados foram carregados corretamente.")
    st.stop()

# Acessa a coluna "Classe" e obtém os valores únicos
classes = ["Todas as Classes"] + df_data["Classe"].unique().tolist()

# Mostra um seletor de caixa de seleção na barra lateral para escolher a classe
selected_class = st.sidebar.selectbox("Classes", classes)

# Adiciona a imagem abaixo do menu na barra lateral
st.sidebar.image("logo.png", use_column_width=True)

# Se "Todas as Classes" não foi selecionada
if selected_class != "Todas as Classes":
    # Filtra os dados para mostrar apenas os jogadores da classe selecionada
    df_players = df_data[df_data["Classe"] == selected_class]
    # Exibe todos os jogadores da classe selecionada
    st.write(df_players)
else:
    # Exibe todos os jogadores de todas as classes
    st.write(df_data)

# Adiciona um texto abaixo dos dados
st.write("Atualizado 15/03/2024 as 19h.")