def validar_dados(vendas, clientes, produtos):
    """
    Realiza validações básicas antes da transformação.
    """

    if vendas.empty:
        raise Exception("Arquivo vendas.csv está vazio.")

    if clientes.empty:
        raise Exception("Arquivo clientes.xlsx está vazio.")

    if produtos.empty:
        raise Exception("Arquivo produtos.csv está vazio.")

    colunas_vendas = [
        "VendaID",
        "ClienteID",
        "ProdutoID",
        "Quantidade",
        "Preço",
        "Valor",
        "Data"
    ]

    for coluna in colunas_vendas:
        if coluna not in vendas.columns:
            raise Exception(
                f"Coluna '{coluna}' não encontrada em vendas.csv"
            )

    colunas_clientes = [
        "ClienteID",
        "Nome",
        "Cidade"
    ]

    for coluna in colunas_clientes:
        if coluna not in clientes.columns:
            raise Exception(
                f"Coluna '{coluna}' não encontrada em clientes.xlsx"
            )

    colunas_produtos = [
        "ProdutoID",
        "Nome",
        "Categoria",
        "Preço"
    ]

    for coluna in colunas_produtos:
        if coluna not in produtos.columns:
            raise Exception(
                f"Coluna '{coluna}' não encontrada em produtos.csv"
            )

    print("Validação concluída com sucesso.")