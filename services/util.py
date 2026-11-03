from datetime import datetime


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo não pode ficar vazio.")


def ler_inteiro(mensagem, minimo=1):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Digite um número maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_valor(mensagem, minimo=0):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor >= minimo:
                return valor
            print(f"Digite um valor maior ou igual a {minimo}.")
        except ValueError:
            print("Digite um valor numérico válido.")


def ler_data(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            datetime.strptime(valor, "%d/%m/%Y")
            return valor
        except ValueError:
            print("Use o formato DD/MM/AAAA.")


def data_obj(valor):
    return datetime.strptime(valor, "%d/%m/%Y").date()
