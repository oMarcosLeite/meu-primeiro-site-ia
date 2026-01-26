import streamlit as st

# 1. ISSO PRECISA SER A PRIMEIRA LINHA: Configura o layout largo
st.set_page_config(page_title="Cacau", layout="wide")

# 2. ESTILO PARA LIMPAR O TOPO (CSS)
st.markdown("""
    <style>
    .main { background-color: #F0F2F6; }
    /* Remove o espaço vazio exagerado no topo do Streamlit */
    .block-container { padding-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. O CABEÇALHO (Título no Topo)
# Usamos HTML para garantir que ele fique elegante e à esquerda
# --- 1. CABEÇALHO (Já está no topo) ---
st.markdown("""
    <h1 style='text-align: left; font-family: serif; color: #2C2C2C; font-size: 45px; margin-bottom: 0px;'>
        Cacau
    </h1>
""", unsafe_allow_html=True)

st.markdown("---")

# --- 2. CONTEÚDO PRINCIPAL (Sem botões, aparece direto) ---
# Note que agora não tem mais "if" nem "with". O código está encostado na esquerda.

st.title("🏡 Portal Cacau Imob")

# Coloque aqui o nome da sua foto que está no GitHub
st.image("foto3.jpeg", use_container_width=500)

st.write("Bem-vindo ao nosso refúgio exclusivo. Explore nossa curadoria de imóveis.")

# Aqui você pode continuar colocando o restante do conteúdo (vitrine, etc)

# --- PÁGINA INICIAL ---
# --- PÁGINA INICIAL (VITRINE) ---
# --- LOGICA DAS PÁGINAS ---

