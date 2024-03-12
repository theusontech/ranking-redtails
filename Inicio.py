import streamlit as st
import pandas as pd

# Definir o título da página
st.set_page_config(page_title="Redtails Dashboard made by: Dellan")

# Carregar os dados se não estiverem na sessão
if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/ranking.csv", index_col=0)
    st.session_state["data"] = df_data

# Escrever o conteúdo principal
st.write("# Ranking de membros RedTails:crossed_swords:")
st.write("""
Este projeto é da guild RedTails do Ragnarok Origin, que busca atualizar e mostrar o ranking dos jogadores dentro da guild. Futuramente, serão implementadas novas atualizações.
""")

# Adicionar conteúdo à barra lateral
st.sidebar.write("Este é um projeto para a Guild RedTails para visualização de membros, ranking, level e contribuição")
