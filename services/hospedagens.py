from data import banco
from models.hospedagem import Hospedagem
from services.util import ler_inteiro, ler_data, data_obj
from services.passageiros import listar_passageiros, obter_passageiro
from services.hoteis import listar_hoteis, obter_hotel


def criar_hospedagem():

    if not banco.passageiros or not banco.hoteis:
        print("Cadastre passageiros e hotéis antes.")
        return

    listar_passageiros()

    pid = ler_inteiro("ID do passageiro: ")
    if not obter_passageiro(pid):
        print("Passageiro não encontrado.")
        return
    
    listar_hoteis()
    hid = ler_inteiro("ID do hotel: ")
    hotel = obter_hotel(hid)
    
    if not hotel:
        print("Hotel não encontrado.")
        return
    
    elif not hotel.quartos:
        print("Esse hotel ainda não tem quartos.")
        return
    
    for q in hotel.quartos:
        print(q)
    qid = ler_inteiro("ID do quarto: ")
    quarto = next((q for q in hotel.quartos if q.id == qid), None)

    if not quarto:
        print("Quarto não encontrado nesse hotel.")
        return
    
    entrada = ler_data("Entrada (DD/MM/AAAA): ")
    saida = ler_data("Saída (DD/MM/AAAA): ")

    if data_obj(saida) <= data_obj(entrada):
        print("A saída deve ser posterior à entrada.")
        return
    
    for h in banco.hospedagens:
        if (
            h.quarto_id == qid
            and h.ativa
            and data_obj(entrada) < data_obj(h.saida)
            and data_obj(saida) > data_obj(h.entrada)
        ):
            print("Esse quarto já está reservado nesse período.")
            return
        
    noites = (data_obj(saida) - data_obj(entrada)).days
    valor = noites * quarto.diaria

    hospedagem = Hospedagem(
        banco.novo_id("hospedagem"), pid, hid, qid, entrada, saida, valor
    )
    banco.hospedagens.append(hospedagem)
    print(f"Hospedagem criada com ID {hospedagem.id}. Total: R$ {valor:.2f}.")


def listar_hospedagens():
    print("\n--- Hospedagens ---")
    if not banco.hospedagens:
        print("Nenhuma hospedagem cadastrada.")
    for h in banco.hospedagens:
        print(h)


def obter_hospedagem(id_hospedagem):
    return next((h for h in banco.hospedagens if h.id == id_hospedagem), None)


def menu_hospedagens():
    while True:
        print("\n1. Criar hospedagem\n2. Listar hospedagens\n0. Voltar")
        op = input("Opção: ").strip()
        if op == "1":
            criar_hospedagem()
        elif op == "2":
            listar_hospedagens()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
