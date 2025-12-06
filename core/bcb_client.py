# Importação das bibliotecas
# ===============================================================================
from bcb import sgs
import pandas as pd

# Função para obter série temporal do SGS
# ===============================================================================
def get_serie(
        indicador: str,
        start_date: str = None,
        end_date: str = None
        ):
    
    # Importa o dicionário de indicadores do dicionário
    #--------------------------------------------------
    from core.indicadores import indicadores_financeiros

    # Verifica se o indicador existe no dicionário
    #--------------------------------------------------
    if indicador not in indicadores_financeiros:
        raise ValueError(f"O indicador '{indicador}' não foi encontrado")
    
    # Busca o código do indicador no dicionário
    #--------------------------------------------------
    codigo = indicadores_financeiros[indicador]

    df = sgs.get(codes = codigo, start = start_date, end = end_date)

    df = df.rename(columns = {codigo: "value"})

    df = df.reset_index().rename(columns = {"index": "date"})

    return df