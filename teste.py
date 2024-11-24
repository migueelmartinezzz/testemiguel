import streamlit as st

# Função para definir tema claro ou escuro
def set_theme(dark_mode):
    if dark_mode:
        dark_mode_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #000000; /* Fundo preto para o modo escuro */
            color: #FFFFFF; /* Texto branco */
        }
        [data-testid="stSidebar"] {
            background-color: #FFFFFF; /* Barra lateral branca */
            border-right: 4px solid #00B2A9; /* Borda azul turquesa */
        }
        [data-testid="stSidebar"] .sidebar-content {
            color: #D9D9D9; /* Cor do texto na barra lateral em modo escuro */
        }
        h1, h2, h3, h4, h5, h6, p, .titulo, .subtitulo {
            color: #FFFFFF; /* Texto branco no modo escuro */
        }
        </style>
        """
        st.markdown(dark_mode_css, unsafe_allow_html=True)
    else:
        light_mode_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #D9D9D9; /* Fundo cinza claro para o modo claro */
            color: #000000; /* Texto preto */
        }
        [data-testid="stSidebar"] {
            background-color: #FFFFFF; /* Barra lateral branca */
            border-right: 4px solid #00B2A9; /* Borda azul turquesa */
        }
        [data-testid="stSidebar"] .sidebar-content {
            color: #000000; /* Texto preto na barra lateral no modo claro */
        }
        h1, h2, h3, h4, h5, h6, p, .titulo, .subtitulo {
            color: #000000; /* Texto preto no modo claro */
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

# Adicionando o título, subtítulo e logo com estilos
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap');

.logo {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 100px; /* Ajuste o tamanho da logo */
    margin-bottom: 10px; /* Diminui o espaço entre a logo e o título */
}

.titulo {
    font-size: 32px; /* Diminui o tamanho do título */
    color: #00B2A9; /* Cor turquesa */
    font-family: 'Fjalla One', sans-serif;
    margin-top: 5px; /* Diminui o espaço acima do título */
    margin-bottom: 5px; /* Diminui o espaço abaixo do título */
}

.subtitulo {
    font-size: 20px; /* Diminui o tamanho do subtítulo */
    font-weight: bold;
    color: #333333; /* Cor para o subtítulo */
    font-family: 'Poppins', sans-serif;
    margin-bottom: 15px; /* Diminui o espaço abaixo do subtítulo */
}

hr {
    border: 0;
    height: 1px;
    background-color: #e0e0e0;
    margin-bottom: 15px; /* Diminui o espaço entre a linha divisória e o conteúdo abaixo */
}
</style>
""", unsafe_allow_html=True)

# Tema inicial e switch de tema
theme_switch()

# Exibindo a logo com a tag HTML <img>
st.markdown('<img src="https://github.com/migueelmartinezzz/testemiguel.py/raw/main/WhatsApp%20Image%202024-11-23%20at%2021.02.03.jpeg" class="logo">', unsafe_allow_html=True)

# Linha divisória entre a logo e o título
st.markdown("<hr>", unsafe_allow_html=True)

# Exibição do título e subtítulo
st.markdown("<h1 class='titulo'>Prospectec</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo'>Encontre parceiros & conheça seus concorrentes</h2>", unsafe_allow_html=True)

# Descrição adicional com alinhamento adequado
st.markdown("<p>Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!</p>", unsafe_allow_html=True)
