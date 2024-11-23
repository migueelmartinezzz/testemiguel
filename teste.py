import streamlit as st
import pandas as pd

# Adicionando o CSS para o interruptor e os estilos do título/subtítulo
toggle_css = """
<style>
/* Estilo do título */
.titulo {
    font-size: 36px;
    color: #013220; /* Verde escuro */
    font-family: 'Poppins', sans-serif;
    text-align: center;
}

.subtitulo {
    font-size: 24px;
    font-weight: bold;
    color: #333333; /* Cinza escuro no tema claro */
    font-family: 'Poppins', sans-serif;
    text-align: center;
    margin-top: -10px;
}

/* Estilo do interruptor no canto superior direito */
.switch-container {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 100;
}

.switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 30px;
}

.switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: 0.4s;
    border-radius: 34px;
}

.slider:before {
    position: absolute;
    content: "";
    height: 22px;
    width: 22px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    transition: 0.4s;
    border-radius: 50%;
}

input:checked + .slider {
    background-color: #2196F3;
}

input:checked + .slider:before {
    transform: translateX(26px);
}
</style>
"""

# Adicionando CSS ao Streamlit
st.markdown(toggle_css, unsafe_allow_html=True)

# Função para alternar o tema
def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Escolher o tema a partir do checkbox
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Exibir o interruptor de tema no canto superior direito
st.markdown(
    """
    <div class="switch-container">
        <label class="switch">
            <input type="checkbox" onchange="window.location.reload()" {checked}>
            <span class="slider"></span>
        </label>
    </div>
    """.replace("{checked}", "checked" if st.session_state.dark_mode else ""),
    unsafe_allow_html=True,
)

# Alterar tema baseado no estado do checkbox
if st.session_state.dark_mode:
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
        color: #013220; /* Verde escuro no tema claro */
    }
    .subtitulo {
        color: #333333; /* Cinza escuro */
    }
    </style>
    """
    st.markdown(light_mode_css, unsafe_allow_html=True)

# Exibição de título e subtítulo
st.markdown("<h1 class='titulo'>Prospectec</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo'>Encontre parceiros e conheça seus concorrentes</h2>", unsafe_allow_html=True)

# Descrição adicional
st.write("Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!")


   
    
