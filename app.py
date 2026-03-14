import streamlit as st

# Configuração da página
st.set_page_config(page_title="Consultor de Obra - Churras Express", layout="wide")

# Estilização personalizada
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stHeading { color: #d32f2f; }
    </style>
    """, unsafe_allow_info=True)

# Cabeçalho
st.title("🏗️ Consultor Técnico: Unidade Assaí Sinop")
st.subheader("Churras Express - Guia de Execução e Instalações")

# Barra Lateral - Navegação
menu = st.sidebar.radio("Selecione a Disciplina:", 
    ["Resumo do Projeto", "Elétrica", "Hidráulica", "Arquitetura/Civil", "FAQ da Obra"])

# --- SEÇÃO: RESUMO ---
if menu == "Resumo do Projeto":
    st.header("📍 Visão Geral")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Localização:** Assaí Sinop")
        st.info("**Tipo de Estrutura:** Container")
    with col2:
        st.info("**Área de Atuação:** Alimentação")
        st.info("**Responsabilidade:** Lojista (Instalações novas)")

# --- SEÇÃO: ELÉTRICA ---
elif menu == "Elétrica":
    st.header("⚡ Especificações Elétricas")
    st.warning("⚠️ Atenção: Sistema Trifásico 380/220V")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Condutores de Entrada")
        st.write("- **Seção:** 3x10mm² + N + T")
        st.write("- **Cabo:** Cobre flexível classe 5, antichama")
        st.write("- **Marcas Referência:** Prysmian (Afumex), Siemens, Conduspar")
    
    with col2:
        st.markdown("### Proteção e Infra")
        st.write("- **Disjuntor Geral:** 50A (Curva C - 15kA)")
        st.write("- **Infraestrutura:** Eletrodutos de aço galvanizado aparente")
        st.write("- **Tomadas/Interruptores:** Pial Legrand (Série Pial Plus)")

# --- SEÇÃO: HIDRÁULICA ---
elif menu == "Hidráulica":
    st.header("🚰 Instalações Hidrossanitárias")
    st.markdown("### Esgoto e Gordura")
    st.write("- **Caixa de Gordura:** 30x30x24cm com tela coletora (em piso)")
    st.write("- **Tubulação:** PVC 50mm para pias")
    st.write("- **Altura Tubulação:** Aparentes a 0,20m do piso acabado")
    
    st.markdown("### Água Fria")
    st.write("- **Medição:** Hidrômetro individual (posicionado entre 0,20m e 1,60m)")
    st.error("Proibido realizar furações na laje ou embutir tubulação em alvenarias externas.")

# --- SEÇÃO: ARQUITETURA ---
elif menu == "Arquitetura/Civil":
    st.header("📐 Detalhes Construtivos")
    st.write("**Piso:** Cerâmico Branco Antiderrapante")
    st.write("**Paredes:** Revestimento cerâmico branco (novo)")
    st.write("**Teto:** Estrutura aparente (sem forro embutido)")
    st.markdown("---")
    st.write("📌 **Nota:** Nenhuma estrutura da galeria (vigas/pilares) pode sofrer interferência.")

# --- SEÇÃO: FAQ ---
elif menu == "FAQ da Obra":
    st.header("💬 Dúvidas Rápidas")
    
    with st.expander("Qual a marca de cabos devo comprar?"):
        st.write("A recomendação principal é **Prysmian (Linha Afumex)**. Siemens e Conduspar também são aceitas.")
        
    with st.expander("Posso quebrar a parede para passar o esgoto?"):
        st.write("Não. O projeto especifica tubulação aparente a 0,20m do piso para evitar danos à estrutura do Mall.")

    with st.expander("Qual o disjuntor para a chopeira?"):
        st.write("O circuito da chopeira deve seguir o diagrama unifilar, utilizando disjuntores curva C (referência Siemens ou Schneider).")
