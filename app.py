import streamlit as st

st.title(body="Input")

botao_input_data = st.date_input(label="Data")

botao_input_sim_nao = st.radio(label="Fez?", options=["Sim", "Não"])

st.write(botao_input_data)

st.write(botao_input_sim_nao)

#TODO: Inserir lógica de inserção e tratamento