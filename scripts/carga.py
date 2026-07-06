import sqlite3

from config import CONFIG


def salvar_sqlite(df):
    """
    Salva o DataFrame no banco SQLite.
    """

    conn = sqlite3.connect(
        CONFIG["paths"]["sqlite"]
    )

    df.to_sql(
        "vendas",
        conn,
        if_exists="replace",
        index=False
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_cliente
        ON vendas (ClienteID)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_produto
        ON vendas (ProdutoID)
    """)

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_data
        ON vendas (Data)
    """)

    conn.commit()
    conn.close()

    print("Banco SQLite criado com sucesso!")