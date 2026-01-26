import streamlit as st

# 1. Configuração básica
st.set_page_config(page_title="Cacau Imob", layout="wide")

# 2. Cor de fundo e limpeza do topo
st.markdown("<style>[data-testid='stAppViewContainer'] {background-color: #FDFCF8 !important;} .block-container {padding-top: 1rem;}</style>", unsafe_allow_html=True)

# 3. Título no topo
st.markdown("<h1 style='font-family: serif; color: #2C2C2C;'>Cacau</h1>", unsafe_allow_html=True)
st.markdown("---")

# 4. A FOTO (Estreita e Centralizada)
# Criamos 3 colunas: as das pontas são largas (3), a do meio é estreita (2)
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.image("foto3.jpeg", use_container_width=True)
    st.write("Bem-vindo ao refúgio exclusivo.")
