import logging
import os


def setup_logger():
    """
    Configura o sistema de logs do pipeline.
    """

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("ETL")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    arquivo = logging.FileHandler(
        "logs/pipeline.log",
        encoding="utf-8"
    )

    console = logging.StreamHandler()

    arquivo.setFormatter(formatter)
    console.setFormatter(formatter)

    logger.addHandler(arquivo)
    logger.addHandler(console)

    return logger