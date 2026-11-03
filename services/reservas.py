from data import banco
from models.reserva import Reserva
from services.util import ler_inteiro, ler_valor
from services.passageiros import listar_passageiros, obter_passageiro
from services.voos import listar_voos, obter_voo


def criar_reserva():
    if not banco.passageiros or not banco.voos:
        print("Cadastre pelo menos um passageiro e um voo antes de reservar.")
        return
    
    listar_passageiros()
    passageiro_id = ler_inteiro("ID do passageiro: ")
    passageiro = obter_passageiro(passageiro_id)
    
    if not passageiro:
        print("Passageiro não encontrado.")
        return
    
    listar_voos()
    voo_id = ler_inteiro("ID do voo: ")
    voo = obter_voo(voo_id)
    if not voo:
        print("Voo não encontrado.")
        return
    
    reservas_ativas = [r for r in banco.reservas if r.voo_id == voo_id and r.ativa]
    if len(reservas_ativas) >= voo.capacidade:
        print("Esse voo já atingiu a capacidade.")
        return
    
    assento = input("Assento (ex.: 12A): ").strip().upper()
    if not assento:
        print("Assento não pode ficar vazio.")
        return
    
    if any(
        r.voo_id == voo_id and r.assento == assento and r.ativa for r in banco.reservas
    ):
        print("Esse assento já está ocupado.")
        return
    
    valor = ler_valor("Valor da passagem (R$): ")
    r = Reserva(banco.novo_id("reserva"), passageiro_id, voo_id, assento, valor)
    banco.reservas.append(r)
    print(f"Reserva criada com ID {r.id}.")


def listar_reservas():
    print("\n--- Reservas aéreas ---")
    if not banco.reservas:
        print("Nenhuma reserva cadastrada.")
    for r in banco.reservas:
        print(r)


def obter_reserva(id_reserva):
    return next((r for r in banco.reservas if r.id == id_reserva), None)


def menu_reservas():
    while True:
        print("\n1. Criar reserva\n2. Listar reservas\n0. Voltar")
        op = input("Opção: ").strip()
        if op == "1":
            criar_reserva()
        elif op == "2":
            listar_reservas()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
