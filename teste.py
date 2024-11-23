import streamlit as st
import pandas as pd
import streamlit as st

# Função para definir tema claro ou escuro
def set_theme(dark_mode):
    if dark_mode:
        dark_mode_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #0e1117;
            color: #ffffff;
        }
        [data-testid="stSidebar"] {
            background-color: #1c1e26;
        }
        h1, h2, h3, h4, h5, h6, p, .titulo, .subtitulo {
            color: #ffffff;
        }
        </style>
        """
        st.markdown(dark_mode_css, unsafe_allow_html=True)
    else:
        light_mode_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #f5f5f5;
            color: #000000;
        }
        [data-testid="stSidebar"] {
            background-color: #ffffff;
        }
        h1, h2, h3, h4, h5, h6, p, .titulo, .subtitulo {
            color: #000000;
        }
        .titulo {
            color: #00B2A9; /* Cor turquesa para o título */
        }
        .subtitulo {
            color: #333333; /* Cinza escuro para o subtítulo */
        }
        </style>
        """
        st.markdown(light_mode_css, unsafe_allow_html=True)

# Adicionando a barra lateral para selecionar o tema
tema = st.sidebar.radio("Escolha o tema", ["Claro", "Escuro"])

# Definindo o tema inicial
if tema == "Escuro":
    set_theme(True)
else:
    set_theme(False)

# Estilos do título e subtítulo
st.markdown("""
<style>
.titulo {
    font-size: 36px;
    font-family: 'Poppins', sans-serif;
    text-align: center;  /* Centralizado */
}

.subtitulo {
    font-size: 24px;
    font-weight: bold;
    font-family: 'Poppins', sans-serif;
    text-align: center;  /* Centralizado */
    margin-top: -10px;
}
</style>
""", unsafe_allow_html=True)

# Exibição do título e subtítulo
st.markdown("<h1 class='titulo'>Prospectec</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo'>Encontre parceiros e conheça seus concorrentes</h2>", unsafe_allow_html=True)

# Descrição adicional
st.write("Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!")

