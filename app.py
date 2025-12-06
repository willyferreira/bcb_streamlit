
# Importação das bibliotecas
# ===============================================================================
import streamlit as st

# Configuração da página
# ===============================================================================
st.set_page_config(
    page_title="Dashboard BCB",
    layout="wide"
)

# Lista de Páginas
# ===============================================================================
focus = st.Page(
    page = "pages/focus.py",
    title = "Relatório Focus"
)
juros_principais = st.Page(
    page = "pages/juros_principais.py",
    title = "Principais Indicadores"
)


# Estrutura de navegação das páginas
# ===============================================================================
pages = st.navigation(
    pages = {
        "Expectativas de Mercado": [focus],
        "Taxas de Juros": [juros_principais]
    },
    position = "top",
    expanded = True
)

# Estrutura de navegação das páginas
# ===============================================================================
pages.run()