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
import streamlit as st

# Escolha de tema
tema = st.sidebar.radio("Escolha o tema", ["Claro", "Escuro"])

# CSS para temas e botão estilizado
if tema == "Escuro":
    dark_mode = """
    <style>
    /* Fundo principal e texto no modo escuro */
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117; /* Fundo escuro */
        color: #ffffff; /* Texto branco */
    }
    [data-testid="stSidebar"] {
        background-color: #1c1e26; /* Fundo da barra lateral */
    }

    /* Ajuste das cores de títulos e parágrafos */
    h1, h2, h3, h4, h5, h6, p, .subtitulo, .titulo {
        color: #ffffff; /* Branco para títulos e textos */
    }

    /* Botão estilizado */
    .stButton button {
        background: linear-gradient(90deg, #1f4037, #99f2c8); /* Gradiente verde */
        color: #ffffff; /* Texto branco */
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 25px; /* Bordas arredondadas */
        cursor: pointer;
        transition: transform 0.2s, background 0.2s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #99f2c8, #1f4037); /* Inverte gradiente no hover */
        transform: scale(1.05); /* Leve aumento no hover */
    }
    </style>
    """
    st.markdown(dark_mode, unsafe_allow_html=True)
else:
    light_mode = """
    <style>
    /* Fundo principal e texto no modo claro */
    [data-testid="stAppViewContainer"] {
        background-color: #f5f5f5; /* Fundo claro */
        color: #000000; /* Texto preto */
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff; /* Fundo da barra lateral */
    }

    /* Ajuste das cores de títulos e parágrafos */
    h1, h2, h3, h4, h5, h6, p, .subtitulo, .titulo {
        color: #000000; /* Preto para títulos e textos */
    }

    /* Botão estilizado */
    .stButton button {
        background: linear-gradient(90deg, #4facfe, #00f2fe); /* Gradiente azul */
        color: #ffffff; /* Texto branco */
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 25px; /* Bordas arredondadas */
        cursor: pointer;
        transition: transform 0.2s, background 0.2s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #00f2fe, #4facfe); /* Inverte gradiente no hover */
        transform: scale(1.05); /* Leve aumento no hover */
    }
    </style>
    """
    st.markdown(light_mode, unsafe_allow_html=True)

# Exemplo de conteúdo no site
st.markdown("<h1 class='titulo'>Prospectec</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo'>Encontre parceiros e conheça seus concorrentes</h2>", unsafe_allow_html=True)
st.write("Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!")
st.button("Clique aqui")

   
    
