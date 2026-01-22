import streamlit as st

st.set_page_config(page_title="PropTech Pro", page_icon="🏢", layout="wide")

# --- BARRA LATERAL (MENU) ---
with st.sidebar:
    st.title("⚙️ Painel de Controle")
    opcao = st.radio(
        "Escolha uma ferramenta:",
        ("Início", "Calculadora de Custos", "Gerador de Checklist", "Formatador de Anúncio")
    )
    st.info("Logado como: Desenvolvedor Imobiliário")

# --- PÁGINA INICIAL ---
if opcao == "Início":
    st.title("🏠 Bem-vindo à sua Plataforma Imobiliária")
    st.write("Esta ferramenta foi criada para automatizar o seu dia a dia e proteger seu foco.")
    st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80")

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
