import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

# HTML e CSS para estilizar o título e subtítulo
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
        font-family: 'Fjalla One', sans-serif;
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
    <div style='text-align: center; font-family: Fjalla One, sans-serif; color: #555555;'>
    Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!
    </div>
    """,
    unsafe_allow_html=True
)




