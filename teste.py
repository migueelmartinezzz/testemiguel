import streamlit as st
import pandas as pd
# HTML e CSS para estilizar apenas o título
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap');
    .titulo {
        font-size: 36px;
        color: #006400; /* Verde escuro */
        font-family: 'Fjalla One', sans-serif; /* Fonte Fjalla One */
        text-align: center; /* Centralizado */
    }
    .subtitulo {
        font-size: 24px;
        font-weight: bold; /* Negrito */
        color: #333333; /* Cinza escuro */
        font-family: 'Poppins', sans-serif; /* Fonte Padrão */
        text-align: center; /* Centralizado */
        margin-top: -10px; /* Ajuste opcional para aproximar o subtítulo */
    }
    </style>
    <h1 class="titulo">Prospectec</h1>
    <h2 class="subtitulo">Encontre parceiros e conheça seus concorrentes</h2>
    """,
    unsafe_allow_html=True
)

# Descrição adicional
st.markdown(
    """
    <div style='text-align: center; font-family: Poppins, sans-serif; color: #555555;'>
    Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!
    </div>
    """,
    unsafe_allow_html=True
)
# Escolha de tema
tema = st.sidebar.radio("Escolha o tema", ["Claro", "Escuro"])

# CSS para temas
if tema == "Escuro":
    dark_mode = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
        color: #ffffff;
    }
    [data-testid="stSidebar"] {
        background-color: #1c1e26;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #ffffff;
    }
    </style>
    """
    st.markdown(dark_mode, unsafe_allow_html=True)
else:
    light_mode = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f5f5f5;
        color: #000000;
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #000000;
    }
    </style>
    """
    st.markdown(light_mode, unsafe_allow_html=True)

