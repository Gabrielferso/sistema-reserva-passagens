from data import banco
from models.passageiro import Passageiro
from services.util import ler_texto


def cadastrar_passageiro():
    print("\n--- Cadastro de passageiro ---")
    nome = ler_texto("Nome: ")
    documento = ler_texto("Documento: ")
    
    if any(p.documento == documento for p in banco.passageiros):
        print("Já existe passageiro com esse documento.")
        return
    
    telefone = ler_texto("Telefone: ")
    email = ler_texto("E-mail: ")
    p = Passageiro(banco.novo_id("passageiro"), nome, documento, telefone, email)
    banco.passageiros.append(p)
    print(f"Passageiro cadastrado com ID {p.id}.")


def listar_passageiros():
    print("\n--- Passageiros ---")
    if not banco.passageiros:
        print("Nenhum passageiro cadastrado.")
    for p in banco.passageiros:
        print(p)


def obter_passageiro(id_passageiro):
    return next((p for p in banco.passageiros if p.id == id_passageiro), None)


def menu_passageiros():
    while True:
        print("\n1. Cadastrar passageiro\n2. Listar passageiros\n0. Voltar")
        op = input("Opção: ").strip()
        if op == "1":
            cadastrar_passageiro()
        elif op == "2":
            listar_passageiros()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
