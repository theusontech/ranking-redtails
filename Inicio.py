import streamlit as st
import pandas as pd

# Define o título da página exibido na barra do navegador
st.set_page_config(page_title="Ranking RedTails")

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/ranking.csv", index_col=0)
    st.session_state["data"] = df_data

st.write("# Ranking de membros RedTails:crossed_swords:")
st.write("""
Este projeto é da guild RedTails do Ragnarok Origin, que busca atualizar e mostrar o ranking dos jogadores dentro da guild. Futuramente, serão implementadas novas atualizações.
""")
st.sidebar.write("Esse é um prjeto para a Guild Redtails para visualização de membros, ranking, level e contribuição")
# Adiciona a imagem abaixo do menu na barra lateral
st.sidebar.image("logo.png", use_column_width=True)