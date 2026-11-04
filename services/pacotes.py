from data import banco
from data.persistencia import salvar_banco
from models.pacote import Pacote
from services.util import ler_inteiro, ler_valor, data_obj
from services.reservas import listar_reservas, obter_reserva
from services.hospedagens import listar_hospedagens, obter_hospedagem
from services.voos import obter_voo


def criar_pacote():
    reservas = [r for r in banco.reservas if r.ativa]
    hospedagens = [h for h in banco.hospedagens if h.ativa]
    
    if not reservas or not hospedagens:
        print("É necessário ter uma reserva ativa e uma hospedagem ativa.")
        return
    
    listar_reservas()
    rid = ler_inteiro("ID da reserva aérea: ")
    reserva = obter_reserva(rid)
    
    if not reserva or not reserva.ativa:
        print("Reserva ativa não encontrada.")
        return
    
    listar_hospedagens()
    hid = ler_inteiro("ID da hospedagem: ")
    hospedagem = obter_hospedagem(hid)
    
    if not hospedagem or not hospedagem.ativa:
        print("Hospedagem ativa não encontrada.")
        return
    
    if reserva.passageiro_id != hospedagem.passageiro_id:
        print("A reserva e a hospedagem precisam pertencer ao mesmo passageiro.")
        return
    
    voo = obter_voo(reserva.voo_id)
    
    if voo and (
        data_obj(hospedagem.entrada) > data_obj(voo.data)
        or data_obj(hospedagem.saida) <= data_obj(voo.data)
    ):
        print("A hospedagem deve abranger a data do voo.")
        return
    
    if any(
        p.ativo and (p.reserva_id == rid or p.hospedagem_id == hid)
        for p in banco.pacotes
    ):
        print("Essa reserva ou hospedagem já está associada a outro pacote.")
        return
    
    valor = ler_valor("Valor adicional do pacote (R$): ")
    pacote = Pacote(banco.novo_id("pacote"), rid, hid, valor)
    banco.pacotes.append(pacote)
    salvar_banco()
    print(f"Pacote criado com ID {pacote.id}.")


def listar_pacotes():
    print("\n--- Pacotes de viagem ---")
    if not banco.pacotes:
        print("Nenhum pacote cadastrado.")
    for p in banco.pacotes:
        print(p)


def menu_pacotes():
    while True:
        print("\n1. Criar pacote\n2. Listar pacotes\n0. Voltar")
        op = input("Opção: ").strip()
        if op == "1":
            criar_pacote()
        elif op == "2":
            listar_pacotes()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
