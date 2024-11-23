import streamlit as st
import pandas as pd
st.markdown(
    """
    <style>
    @import url('https://fonts.google.com/share?selection.family=Bokor|Fjalla+One|Noto+Serif:ital,wght@0,100..900;1,100..900r');
    .titulo {
        font-size: 36px;
        color: #003366; /* Azul escuro */
        font-family: 'Poppins', sans-serif; /* Fonte personalizada */
        text-align: center; /* Centralizado */
    }
    .subtitulo {
        font-size: 24px;
        font-weight: bold; /* Negrito */
        color: #333333; /* Cinza escuro */
        font-family: 'Poppins', sans-serif;
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
st.markdown("Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!")



