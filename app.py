import streamlit as st

# Configuração da página (o que aparece na aba do navegador)
st.set_page_config(page_title="Minha PropTech", page_icon="🏠")

# Título Principal
st.title("🚀 Assistente de Tecnologia Imobiliária")
st.subheader("Transformando o mercado com IA e automação")

# Uma linha divisória para organizar o visual
st.divider()

# Área de entrada de dados
st.write("### Teste de Automação de Anúncio")
descricao_bruta = st.text_area("Cole aqui as características do imóvel (ex: 2 qtos, suite, centro):")

# Botão que simula a ação da IA
if st.button("Gerar Texto para Anúncio"):
    if descricao_bruta:
        # Aqui, no futuro, conectaremos a API do ChatGPT
        # Por enquanto, ele apenas mostra que o sistema recebeu os dados
        st.success("Sistema processando... (Aqui entrará a inteligência artificial)")
        st.write(f"**Análise recebida:** {descricao_bruta}")
    else:
        st.warning("Por favor, digite algo para processar.")

# Rodapé simples
st.sidebar.info("Este é o protótipo do seu futuro sistema de IA.")
