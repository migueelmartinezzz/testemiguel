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
            background-color: #333333; /* Barra lateral escura */
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
            color: #003D66; /* Cor Azul Escuro para o título */
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
    display: inline-block;
    width: 100px; /* Ajuste o tamanho da logo */
    margin-right: 20px; /* Espaçamento entre a logo e o título */
}

.titulo {
    font-size: 50px; /* Diminui o tamanho do título */
    color: #003D66; /* Cor Azul Escuro */
    font-family: 'Fjalla One', sans-serif;
    margin-top: 10px; /* Diminui o espaço acima do título */
    margin-bottom: 0px; /* Reduz a distância entre título e subtítulo */
    display: inline-block;
}

.subtitulo {
    font-size: 30px; /* Diminui o tamanho do subtítulo */
    font-weight: bold;
    color: #333333; /* Cor para o subtítulo */
    font-family: 'Poppins', sans-serif;
    margin-top: 0px; /* Reduz a distância entre subtítulo e conteúdo */
    margin-bottom: 10px; /* Reduz a distância entre o subtítulo e o conteúdo */
}

hr {
    border: 0;
    height: 5px;
    background-color: #00B2A9;
    margin-bottom: 10px; /* Diminui o espaço entre a linha divisória e o conteúdo abaixo */
}
</style>
""", unsafe_allow_html=True)

# Tema inicial e switch de tema
theme_switch()

# Exibindo o título e a logo lado a lado
st.markdown('<div style="display: flex; align-items: center;">'
            '<img src="https://github.com/migueelmartinezzz/testemiguel.py/raw/main/WhatsApp%20Image%202024-11-23%20at%2021.02.03.jpeg" class="logo">'
            '<h1 class="titulo">Prospectec</h1>'
            '</div>', unsafe_allow_html=True)

# Linha divisória entre o título/logo e o subtítulo
st.markdown("<hr>", unsafe_allow_html=True)

# Exibição do subtítulo
st.markdown("<h2 class='subtitulo'>Encontre parceiros & conheça seus concorrentes</h2>", unsafe_allow_html=True)

# Descrição adicional com alinhamento adequado
st.markdown("<p>Utilize nossa ferramenta para identificar empresas semelhantes em poucos cliques!</p>", unsafe_allow_html=True)

