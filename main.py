import os

from config import CONFIG
from scripts.logger import setup_logger
from scripts.gerar_dados import gerar_dados
from scripts.extracao import extrair_dados
from scripts.validacao import validar_dados
from scripts.transformacao import transformar_dados
from scripts.carga import salvar_sqlite
from scripts.relatorio import gerar_relatorios


def criar_pastas():

    os.makedirs(CONFIG["paths"]["dados"], exist_ok=True)
    os.makedirs(CONFIG["paths"]["banco"], exist_ok=True)
    os.makedirs(CONFIG["paths"]["relatorios"], exist_ok=True)


def main():

    criar_pastas()

    logger = setup_logger()

    try:

        logger.info("========== INÍCIO DO PIPELINE ==========")

        logger.info("Gerando dados fictícios...")
        gerar_dados()

        logger.info("Extraindo dados...")
        vendas, clientes, produtos = extrair_dados()

        logger.info("Validando dados...")
        validar_dados(vendas, clientes, produtos)

        logger.info("Transformando dados...")
        dados = transformar_dados(
            vendas,
            clientes,
            produtos
        )

        logger.info("Salvando SQLite...")
        salvar_sqlite(dados)

        logger.info("Gerando relatórios...")
        gerar_relatorios(dados)

        logger.info("PIPELINE FINALIZADO COM SUCESSO!")

    except Exception as erro:

        logger.exception(erro)


if __name__ == "__main__":
    main()