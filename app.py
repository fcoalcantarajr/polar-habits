# Import necessary libraries
import streamlit as st
import pandas as pd
import datetime

# Define a function to update the control list with new data
def atualizar_tabela(botao_input_data: datetime.date, botao_input_sim_nao: str):
    # Cast the current DataFrame from session to ensure it is a DataFrame, and append a new row.
    df_temp = pd.DataFrame(st.session_state.df)
    new_row = pd.DataFrame({"data": [botao_input_data], "sim_nao": [botao_input_sim_nao]})
    df_updated = pd.concat([df_temp, new_row], ignore_index=True)
    st.session_state.df = df_updated

# Initialize your DataFrame in session state if it has not been already
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({
        "data": [],
        "sim_nao": []
    })

# Set the title of the input form
st.title("Input")

# Create a form to get input from the user
with st.form(key="Input"):
    botao_input_data = st.date_input(label="Data")  # Input for date
    botao_input_sim_nao = st.radio(label="Fez?", options=["Sim", "Não"])  # Radio button for "Yes" or "No"

    button = st.form_submit_button(label="Atualizar")  # Submit button for updating

    if button:
        atualizar_tabela(botao_input_data, botao_input_sim_nao)  # Call the function to update the control list

    # Use the session state DataFrame to display
    st.write(st.session_state.df)