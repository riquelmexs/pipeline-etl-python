import pandas as pd


def transformar_dados(vendas, clientes, produtos):
    """
    Limpeza e transformação dos dados.
    """

    
    vendas = vendas.drop_duplicates()

    clientes = clientes.drop_duplicates()

    produtos = produtos.drop_duplicates()

    
    clientes["Nome"] = clientes["Nome"].str.strip()

    
    vendas["Data"] = pd.to_datetime(
        vendas["Data"],
        errors="coerce"
    )

    
    clientes["Cidade"] = clientes["Cidade"].fillna(
        "Não informado"
    )

    vendas["Quantidade"] = vendas["Quantidade"].fillna(0)

    vendas["Preço"] = vendas["Preço"].fillna(
        vendas["Preço"].mean()
    )

    
    vendas = vendas.dropna(subset=["Data"])

    
    vendas["Total"] = (
        vendas["Quantidade"] *
        vendas["Preço"]
    )

    
    dados = vendas.merge(
        clientes,
        on="ClienteID",
        how="left"
    )

    
    dados = dados.merge(
        produtos,
        on="ProdutoID",
        how="left"
    )

    
    dados = dados.rename(
        columns={
            "Nome_x": "Cliente",
            "Nome_y": "Produto"
        }
    )

    
    dados = dados.sort_values("Data")

    return dados