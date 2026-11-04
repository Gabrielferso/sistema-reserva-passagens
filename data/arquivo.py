
from pathlib import Path
from urllib.parse import quote, unquote

PASTA_DADOS = Path(__file__).resolve().parent.parent / "dados"


def salvar_dados(nome_arquivo, registros):
    PASTA_DADOS.mkdir(exist_ok=True)

    caminho = PASTA_DADOS / nome_arquivo

    with open(caminho, "w", encoding="utf-8") as arquivo:
        for registro in registros:
            campos = [quote(str(valor), safe="") for valor in registro]
            arquivo.write(";".join(campos) + "\n")


def carregar_dados(nome_arquivo):
    caminho = PASTA_DADOS / nome_arquivo

    if not caminho.exists():
        return []

    registros = []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.rstrip("\n")

            if linha:
                campos = linha.split(";")
                registros.append([unquote(campo) for campo in campos])

    return registros
