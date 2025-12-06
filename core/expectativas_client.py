import pandas as pd
from bcb import Expectativas
from core.indicadores import expectativas_indicadores

def get_expectativas_mercado_anuais(indicador: str, data = None) -> pd.DataFrame:

    # Verifica se o indicador existe no dicionário
    if indicador not in expectativas_indicadores:
        raise ValueError(f"O indicador '{indicador}' não foi encontrado no dicionário de dados.")
    
    if data is None:
        raise ValueError(f"Favor informar a data'{data}'.")


    em = Expectativas()

    # Obtém o endpoint
    ep = em.get_endpoint("ExpectativasMercadoAnuais")

    # Consulta o indicador escolhido
    df = (
        ep.query()
        .select(ep.Indicador, ep.Data, ep.DataReferencia, ep.Mediana)
        .filter(ep.Indicador == indicador)
        .filter(ep.Data >= data)
        .filter(ep.baseCalculo == 0)
        .limit(50)
        .collect()
        )
    df = pd.DataFrame(df)

    return df
