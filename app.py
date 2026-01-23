import streamlit as st
# Estilo personalizado para parecer um site profissional
st.markdown("""
    <style>
    .main {
        background-color: #FDFCF8;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="PropTech Pro", page_icon="🏢", layout="wide")
# Agora o rádio de opções aparece no centro da página
with col_menu:
    opcao = st.radio(
        "", 
        ("Locação", "Venda", "Lançamento"),
        horizontal=True,
        label_visibility="collapsed"
    )
# --- PÁGINA INICIAL ---
# --- PÁGINA INICIAL (VITRINE) ---
if opcao == "Início":
    st.title("🏡 Portal Cacau Imob")
    st.markdown("---")
    st.image("foto1.jpg", use_container_width=True)
    st.divider()
    # Destaque principal
    st.subheader("Destaques da Semana")
    
    # Criando colunas para os imóveis (Parece um site real)
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://images.unsplash.com/photo-1570129477492-45c003edd2be?auto=format&fit=crop&w=500&q=80")
        st.markdown("### Casa de Condomínio - R$ 850.000")
        st.write("📍 Localização: Jardim América")
        if st.button("Ver Detalhes (Imóvel 1)"):
            st.info("Aqui a IA poderia resumir o histórico deste imóvel para você.")

    with col2:
        st.image("https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=500&q=80")
        st.markdown("### Cobertura Duplex - R$ 1.200.000")
        st.write("📍 Localização: Vila Nova")
        if st.button("Ver Detalhes (Imóvel 2)"):
            st.info("A IA detectou que este imóvel está 10% abaixo do preço de mercado.")

    st.markdown("---")
    st.write("💡 *Dica do Desenvolvedor: Estas imagens e textos podem ser buscados automaticamente de um banco de dados no futuro.*")
# --- CALCULADORA DE CUSTOS ---
elif opcao == "Calculadora de Custos":
    st.title("💰 Calculadora de Impostos (Simulação)")
    valor_venda = st.number_input("Valor de Venda do Imóvel (R$):", min_value=0.0, step=10000.0)
    itbi_percent = st.slider("Alíquota ITBI (%)", 1.0, 4.0, 2.0)
    
    if valor_venda > 0:
        itbi_total = valor_venda * (itbi_percent / 100)
        escritura_est = 5000.0  # Valor fictício para o exemplo
        st.metric("Estimativa ITBI", f"R$ {itbi_total:,.2f}")
        st.write(f"**Total aproximado de taxas:** R$ {itbi_total + escritura_est:,.2f}")

# --- GERADOR DE CHECKLIST ---
elif opcao == "Gerador de Checklist":
    st.title("📋 Checklist de Documentos")
    tipo = st.selectbox("Tipo de Vendedor:", ["Pessoa Física", "Pessoa Jurídica"])
    
    if tipo == "Pessoa Física":
        st.checkbox("RG e CPF")
        st.checkbox("Certidão de Casamento/Nascimento")
        st.checkbox("Comprovante de Residência")
        st.checkbox("Certidões Negativas (Justiça Federal, Cível, etc)")
    else:
        st.checkbox("Contrato Social")
        st.checkbox("Cartão CNPJ")
        st.checkbox("Certidão Negativa de Débitos Previdenciários")

# --- FORMATADOR DE ANÚNCIO ---
elif opcao == "Formatador de Anúncio":
    st.title("✍️ Limpeza de Texto")
    texto_sujo = st.text_area("Cole aqui o texto bagunçado do imóvel:")
    if st.button("Limpar e Formatar"):
        # Exemplo de lógica simples de limpeza
        texto_limpo = texto_sujo.replace("!!!", "!").strip().capitalize()
        st.code(texto_limpo, language=None)
        st.success("Texto pronto para copiar!")
