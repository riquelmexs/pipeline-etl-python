import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG = {
    "paths": {
        "dados": os.path.join(BASE_DIR, "dados"),
        "banco": os.path.join(BASE_DIR, "banco"),
        "relatorios": os.path.join(BASE_DIR, "relatorios"),

        "vendas": os.path.join(BASE_DIR, "dados", "vendas.csv"),
        "clientes": os.path.join(BASE_DIR, "dados", "clientes.xlsx"),
        "produtos": os.path.join(BASE_DIR, "dados", "produtos.csv"),

        "sqlite": os.path.join(BASE_DIR, "banco", "empresa.db"),

        "relatorio_excel": os.path.join(BASE_DIR, "relatorios", "relatorio.xlsx"),
        "relatorio_csv": os.path.join(BASE_DIR, "relatorios", "relatorio.csv")
    }
}