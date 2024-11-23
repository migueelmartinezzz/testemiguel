import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

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
# Aba de busca de empresas
with abas[0]:
    st.header("Busca de Empresas")
    
    # Layout dos filtros em colunas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        porte_selecionado = st.selectbox("Porte da Empresa", df['porte_empresa'].unique())
    with col2:
        tempo_selecionado = st.selectbox("Tempo de Criação", df['tempo_criacao'].unique())
    with col3:
        nicho_selecionado = st.selectbox("Nicho", df['nicho'].unique())
    with col4:
        estado_selecionado = st.selectbox("Estado", df['sigla_uf'].unique())

    try:
        # Filtrar o DataFrame com base nas seleções
        df_filtrado = df[
            (df['porte_empresa'] == porte_selecionado) &
            (df['tempo_criacao'] == tempo_selecionado) &
            (df['nicho'] == nicho_selecionado) &
            (df['sigla_uf'] == estado_selecionado)
        ]

        # Sortear o número de resultados a 20
        df_filtrado = df_filtrado.sample(20)

        # Exibir resultados
        st.write("Resultados da Busca:")

        # Loop para exibir os resultados em um formato mais legível
        for index, row in df_filtrado.iterrows():
            st.write(f"**Nome da Empresa:** {row['razao_social']}")
            st.write(f"**Nome do Sócio:** {row['nome_socio']}")
            st.write(f"**Email da Empresa:** {row['email'] if pd.notnull(row['email']) else 'Não disponível'}")
            st.write(f"**Telefone:** {row['telefone'] if pd.notnull(row['telefone']) else 'Não disponível'}")
            st.write("---")  # Linha separadora
    except:
        st.error("Nenhum resultado encontrado. Ajuste os filtros.")

# Rodapé
st.markdown("---")
st.markdown("### Ajude-nos a melhorar!")
st.write("Avalie nossa ferramenta com estrelas e deixe um comentário:")

# Avaliação por estrelas simulada
stars = st.radio(
    "Avaliação (1 - 5 estrelas):",
    options=[1, 2, 3, 4, 5],
    index=4,
    horizontal=True,
)

# Comentário do usuário
comentario = st.text_area("Deixe seu comentário (opcional):")

# Botão para enviar
if st.button("Enviar Avaliação"):
    st.success(f"Obrigado! Você avaliou a ferramenta com {stars} estrelas.")
    if comentario:
        st.info(f"Comentário recebido: {comentario}")
    else:
        st.info("Nenhum comentário foi enviado.")

# Adicionando um texto final
st.markdown(
    """
    <div style="text-align: center; font-size: 12px; margin-top: 20px; color: #888;">
        © 2024 Prospectec. Todos os direitos reservados.
    </div>
    """,
    unsafe_allow_html=True
)



