import streamlit as st
from core.indicadores import indicadores_financeiros, expectativas_indicadores
from core.expectativas_client import get_expectativas_mercado_anuais

indicador = st.selectbox("Selecione um Indicador Financeiro:", list(expectativas_indicadores.keys()))
data = st.date_input("Data:")

if indicador not in expectativas_indicadores.keys():
    st.error("O indicador selecionado não possui dados de expectativas de mercado disponíveis.")
else:
    df = get_expectativas_mercado_anuais(indicador, data = data)

    if df.empty:
        st.warning("Nenhum dado encontrado para o indicador e data selecionados.")

st.dataframe(df)

