import streamlit as st

# 1. Configuração (Sempre a primeira linha)
st.set_page_config(page_title="Cacau Imob", layout="wide")

# 2. Estilo Visual
st.markdown("""
    <style>
    [data-testid='stAppViewContainer'] {background-color: #FDFCF8 !important;}
    .block-container {padding-top: 1rem;}
    /* Estilo para deixar as abas (tabs) mais elegantes */
    .stTabs [data-baseweb="tab-list"] {gap: 24px;}
    .stTabs [data-baseweb="tab"] {font-family: serif; font-size: 18px; color: #666;}
    </style>
""", unsafe_allow_html=True)

# 3. Título no topo
st.markdown("<h1 style='font-family: serif; color: #2C2C2C; margin-bottom: 0px;'>Cacau</h1>", unsafe_allow_html=True)

# --- 4. A BARRA DE MENUS (Entre o título e a foto) ---
# Criamos as abas aqui
aba_inicio, aba_locacao, aba_venda, aba_sobre = st.tabs(["Início", "Locação", "Venda", "Sobre"])

# Agora colocamos a foto dentro da aba "Início", que é a primeira que aparece
with aba_inicio:
    st.markdown("<br>", unsafe_allow_html=True) # Dá um pequeno espaço
    
    # 5. A FOTO (Ajustada para [1, 4, 1] para não ficar minúscula)
    col1, col2, col3 = st.columns([1, 4, 1])
    
    with col2:
        st.image("foto3.jpeg", use_container_width=True)
        st.write("Bem-vindo ao refúgio exclusivo.")

# Se você quiser colocar algo nas outras abas depois, é só usar 'with aba_locacao:', etc.

