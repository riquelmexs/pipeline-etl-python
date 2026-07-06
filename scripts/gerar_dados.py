import os
import random

import pandas as pd
from faker import Faker

from config import CONFIG

fake = Faker("pt_BR")
random.seed(42)


def gerar_clientes():
    clientes = []

    cidades = [
        "Recife",
        "Olinda",
        "Jaboatão",
        "Paulista",
        "Caruaru",
        "Petrolina",
        "Cabo de Santo Agostinho",
        "Garanhuns",
        "Igarassu",
        "Abreu e Lima"
    ]

    for i in range(1, 201):
        clientes.append({
            "ClienteID": i,
            "Nome": fake.name(),
            "Cidade": random.choice(cidades)
        })

    df_clientes = pd.DataFrame(clientes)

    df_clientes.to_excel(
        CONFIG["paths"]["clientes"],
        index=False
    )

    return df_clientes


def gerar_produtos():
    produtos = [
        [1, "Notebook Dell", "Informática", 4200],
        [2, "Notebook Lenovo", "Informática", 3900],
        [3, "Mouse Gamer", "Periféricos", 180],
        [4, "Teclado Mecânico", "Periféricos", 320],
        [5, "Monitor 24", "Monitores", 1100],
        [6, "Monitor 27", "Monitores", 1700],
        [7, "SSD 1TB", "Hardware", 480],
        [8, "HD 2TB", "Hardware", 420],
        [9, "Headset Gamer", "Áudio", 350],
        [10, "Webcam Full HD", "Vídeo", 270],
        [11, "Impressora Epson", "Escritório", 980],
        [12, "Cadeira Gamer", "Móveis", 1550],
        [13, "Mesa Escritório", "Móveis", 870],
        [14, "Microfone USB", "Áudio", 450],
        [15, "Placa de Vídeo RTX", "Hardware", 5200]
    ]

    df_produtos = pd.DataFrame(
        produtos,
        columns=[
            "ProdutoID",
            "Nome",
            "Categoria",
            "Preço"
        ]
    )

    df_produtos.to_csv(
        CONFIG["paths"]["produtos"],
        index=False,
        encoding="utf-8-sig"
    )

    return df_produtos


def gerar_vendas(produtos):
    vendas = []

    for venda_id in range(1, 5001):

        produto = produtos.sample(n=1).iloc[0]

        quantidade = random.randint(1, 5)

        preco = float(produto["Preço"])

        vendas.append({
            "VendaID": venda_id,
            "ClienteID": random.randint(1, 200),
            "ProdutoID": int(produto["ProdutoID"]),
            "Quantidade": quantidade,
            "Preço": preco,
            "Valor": quantidade * preco,
            "Data": fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        })

    df_vendas = pd.DataFrame(vendas)

    df_vendas["Data"] = pd.to_datetime(df_vendas["Data"])

    df_vendas.to_csv(
        CONFIG["paths"]["vendas"],
        index=False,
        encoding="utf-8-sig"
    )

    return df_vendas


def gerar_dados():
    os.makedirs(CONFIG["paths"]["dados"], exist_ok=True)

    print("Gerando clientes...")
    clientes = gerar_clientes()

    print("Gerando produtos...")
    produtos = gerar_produtos()

    print("Gerando vendas...")
    vendas = gerar_vendas(produtos)

    print("-" * 40)
    print(f"Clientes: {len(clientes)}")
    print(f"Produtos: {len(produtos)}")
    print(f"Vendas: {len(vendas)}")
    print("-" * 40)
    print("Dados gerados com sucesso!")


if __name__ == "__main__":
    gerar_dados()