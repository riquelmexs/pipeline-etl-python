import pandas as pd
from config import CONFIG


def extrair_dados():
    """
    Extrai os arquivos CSV e Excel.
    """

    vendas = pd.read_csv(CONFIG["paths"]["vendas"])

    clientes = pd.read_excel(
        CONFIG["paths"]["clientes"]
    )

    produtos = pd.read_csv(
        CONFIG["paths"]["produtos"]
    )

    return vendas, clientes, produtos