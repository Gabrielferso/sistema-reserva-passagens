from services.passageiros import menu_passageiros
from services.voos import menu_voos
from services.reservas import menu_reservas
from services.hoteis import menu_hoteis
from services.hospedagens import menu_hospedagens
from services.pacotes import menu_pacotes
from services.pedidos import menu_pedidos


def executar_menu():
    while True:
        print("""
========================================
 IN-DOALI - SISTEMA DE RESERVAS
========================================
1. Passageiros
2. Voos e infraestrutura aérea
3. Reservas aéreas
4. Hotéis e quartos
5. Hospedagens
6. Pacotes de viagem
7. Consulta de pedidos e cancelamentos
0. Sair
""")
        op = input("Escolha uma opção: ").strip()
        if op == "1":
            menu_passageiros()
        elif op == "2":
            menu_voos()
        elif op == "3":
            menu_reservas()
        elif op == "4":
            menu_hoteis()
        elif op == "5":
            menu_hospedagens()
        elif op == "6":
            menu_pacotes()
        elif op == "7":
            menu_pedidos()
        elif op == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")
