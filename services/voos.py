from data import banco
from models.voo import Voo
from services.util import ler_texto, ler_inteiro, ler_data
from services.passageiros import obter_passageiro


def cadastrar_voo():
    print("\n--- Cadastro de voo ---")
    origem = ler_texto("Aeroporto/cidade de origem: ")
    destino = ler_texto("Aeroporto/cidade de destino: ")
    
    if origem.lower() == destino.lower():
        print("Origem e destino devem ser diferentes.")
        return
    
    data = ler_data("Data (DD/MM/AAAA): ")
    horario = ler_texto("Horário (HH:MM): ")
    aeronave = ler_texto("Aeronave: ")
    capacidade = ler_inteiro("Capacidade de passageiros: ")
    voo = Voo(
        banco.novo_id("voo"), origem, destino, data, horario, aeronave, capacidade
    )
    banco.voos.append(voo)
    print(f"Voo cadastrado com ID {voo.id}.")


def listar_voos():
    print("\n--- Voos ---")
    if not banco.voos:
        print("Nenhum voo cadastrado.")
    for voo in banco.voos:
        print(voo)


def consultar_passageiros_voo():
    if not banco.voos:
        print("Cadastre um voo primeiro.")
        return
    listar_voos()
    
    try:
        id_voo = int(input("ID do voo: "))
    except ValueError:
        print("ID inválido.")
        return
    voo = next((v for v in banco.voos if v.id == id_voo), None)
    
    if not voo:
        print("Voo não encontrado.")
        return
    reservas = [r for r in banco.reservas if r.voo_id == id_voo and r.ativa]
    print(f"Passageiros com reserva ativa no voo {id_voo}:")
    
    if not reservas:
        print("Nenhum passageiro associado.")
    for r in reservas:
        p = obter_passageiro(r.passageiro_id)
        if p:
            print(f"- {p.nome} | Assento {r.assento}")


def obter_voo(id_voo):
    return next((v for v in banco.voos if v.id == id_voo), None)


def menu_voos():
    while True:
        print(
            "\n1. Cadastrar voo\n2. Listar voos\n3. Consultar passageiros de um voo\n0. Voltar"
        )
        op = input("Opção: ").strip()
        if op == "1":
            cadastrar_voo()
        elif op == "2":
            listar_voos()
        elif op == "3":
            consultar_passageiros_voo()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
