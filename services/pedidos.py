from data import banco
from services.reservas import listar_reservas, obter_reserva
from services.hospedagens import listar_hospedagens, obter_hospedagem
from services.pacotes import listar_pacotes


def consultar_pedidos():
    listar_reservas()
    listar_hospedagens()
    listar_pacotes()


def cancelar_pedido():
    print("\n1. Cancelar reserva aérea\n2. Cancelar hospedagem\n3. Cancelar pacote")
    op = input("Tipo de pedido: ").strip()
    
    try:
        pedido_id = int(input("ID do pedido: "))
    except ValueError:
        print("ID inválido.")
        return
    
    if op == "1":
        r = obter_reserva(pedido_id)
        if not r:
            print("Reserva não encontrada.")
        elif not r.ativa:
            print("Reserva já está cancelada.")
        else:
            r.ativa = False
            print("Reserva cancelada.")
    
    elif op == "2":
        h = obter_hospedagem(pedido_id)
        if not h:
            print("Hospedagem não encontrada.")
        elif not h.ativa:
            print("Hospedagem já está cancelada.")
        else:
            h.ativa = False
            print("Hospedagem cancelada.")
    
    elif op == "3":
        p = next((p for p in banco.pacotes if p.id == pedido_id), None)
        if not p:
            print("Pacote não encontrado.")
        elif not p.ativo:
            print("Pacote já está cancelado.")
        else:
            p.ativo = False
            r = obter_reserva(p.reserva_id)
            h = obter_hospedagem(p.hospedagem_id)
            if r:
                r.ativa = False
            if h:
                h.ativa = False
            print("Pacote cancelado, junto com a reserva e a hospedagem associadas.")
    
    else:
        print("Opção inválida.")


def menu_pedidos():
    while True:
        print("\n1. Consultar pedidos\n2. Cancelar pedido\n0. Voltar")
        op = input("Opção: ").strip()
        if op == "1":
            consultar_pedidos()
        elif op == "2":
            cancelar_pedido()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
