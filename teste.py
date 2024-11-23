import streamlit as st
import pandas as pd


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

# Função para criar o interruptor de tema
def theme_switch():
    st.sidebar.markdown("""
    <style>
    .switch-container {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        margin-top: 20px;
    }
    .switch-label {
        margin-right: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .switch {
        position: relative;
        width: 60px;
        height: 30px;
        background-color: #ccc;
        border-radius: 30px;
        transition: background-color 0.3s;
    }
    .switch::before {
        content: "";
        position: absolute;
        top: 50%;
        left: 4px;
        width: 22px;
        height: 22px;
        border-radius: 50%;
        background-color: white;
        transform: translateY(-50%);
        transition: transform 0.3s;
    }
    .switch-on {
        background-color: #00B2A9;
    }
    .switch-on::before {
        transform: translate(30px, -50%);
    }
    </style>
    """, unsafe_allow_html=True)

    # Criar o interruptor de tema
    dark_mode = st.sidebar.checkbox('Modo Escuro', key='theme_toggle')

    if dark_mode:
        st.sidebar.markdown('<div class="switch-container"><label class="switch-label">🌙 Escuro</label><div class="switch switch-on"></div></div>', unsafe_allow_html=True)
        set_theme(True)
    else:
        st.sidebar.markdown('<div class="switch-container"><label class="switch-label">🌞 Claro</label><div class="switch"></div></div>', unsafe_allow_html=True)
        set_theme(False)

# Adicionando o título e subtítulo com fontes personalizadas
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap');

.titulo {
    font-size: 36px;
    color: #00B2A9; /* Cor turquesa */
    font-family: 'Fjalla One', sans-serif;
    text-align: center;
}

.subtitulo {
    font-size: 24px;
    font-weight: bold;
    color: #333333; /* Cor para o subtítulo */
    font-family: 'Poppins', sans-serif;
    text-align: center;
    margin-top: -10px;
}
</style>
""", unsafe_allow_html=True)

# Tema inicial e switch de tema
theme_switch()

# Exibição do título e subtítulo
st.markdown("<h1 class='titulo'>Prospectec</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo'>Encontre parceiros e conheça seus concorrentes</h2>", unsafe_allow_html=True)

# Descrição adicional com alinhamento adequado
st.markdown("<p style='text-align: center;'>Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!</p>", unsafe_allow_html=True)
