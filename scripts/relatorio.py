import pandas as pd
from config import CONFIG


def gerar_relatorios(df):
    """
    Gera relatórios em CSV e Excel.
    """

    faturamento_categoria = (
        df.groupby("Categoria")["Total"]
        .sum()
        .reset_index()
        .sort_values(
            by="Total",
            ascending=False
        )
    )

    faturamento_cidade = (
        df.groupby("Cidade")["Total"]
        .sum()
        .reset_index()
        .sort_values(
            by="Total",
            ascending=False
        )
    )

    top_clientes = (
        df.groupby("Cliente")["Total"]
        .sum()
        .reset_index()
        .sort_values(
            by="Total",
            ascending=False
        )
        .head(10)
    )

    top_produtos = (
        df.groupby("Produto")["Total"]
        .sum()
        .reset_index()
        .sort_values(
            by="Total",
            ascending=False
        )
        .head(10)
    )

    with pd.ExcelWriter(
        CONFIG["paths"]["relatorio_excel"],
        engine="xlsxwriter"
    ) as writer:

        faturamento_categoria.to_excel(
            writer,
            sheet_name="Categoria",
            index=False
        )

        faturamento_cidade.to_excel(
            writer,
            sheet_name="Cidade",
            index=False
        )

        top_clientes.to_excel(
            writer,
            sheet_name="Top Clientes",
            index=False
        )

        top_produtos.to_excel(
            writer,
            sheet_name="Top Produtos",
            index=False
        )

        df.to_excel(
            writer,
            sheet_name="Base Completa",
            index=False
        )

    df.to_csv(
        CONFIG["paths"]["relatorio_csv"],
        index=False,
        encoding="utf-8-sig"
    )

    print("Relatórios gerados com sucesso!")