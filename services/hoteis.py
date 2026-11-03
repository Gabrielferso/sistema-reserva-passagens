from data import banco
from models.hotel import Hotel
from models.quarto import Quarto
from services.util import ler_texto, ler_inteiro, ler_valor


def cadastrar_hotel():
    nome = ler_texto("Nome do hotel: ")
    cidade = ler_texto("Cidade: ")
    hotel = Hotel(banco.novo_id("hotel"), nome, cidade)
    banco.hoteis.append(hotel)
    print(f"Hotel cadastrado com ID {hotel.id}.")


def listar_hoteis():
    print("\n--- Hotéis e quartos ---")
    if not banco.hoteis:
        print("Nenhum hotel cadastrado.")
    for h in banco.hoteis:
        print(h)
        for q in h.quartos:
            print("   ", q)


def obter_hotel(id_hotel):
    return next((h for h in banco.hoteis if h.id == id_hotel), None)


def obter_quarto(id_quarto):
    for h in banco.hoteis:
        for q in h.quartos:
            if q.id == id_quarto:
                return h, q
    return None, None


def cadastrar_quarto():
    if not banco.hoteis:
        print("Cadastre um hotel primeiro.")
        return
    
    listar_hoteis()
    id_hotel = ler_inteiro("ID do hotel: ")
    hotel = obter_hotel(id_hotel)
    if not hotel:
        print("Hotel não encontrado.")
        return
    
    numero = ler_texto("Número/nome do quarto: ")
    if any(q.numero == numero for q in hotel.quartos):
        print("Esse número de quarto já existe nesse hotel.")
        return
    
    capacidade = ler_inteiro("Capacidade de hóspedes: ")
    diaria = ler_valor("Valor da diária (R$): ")
    quarto = Quarto(banco.novo_id("quarto"), numero, capacidade, diaria)
    hotel.quartos.append(quarto)
    print(f"Quarto cadastrado com ID {quarto.id}.")


def menu_hoteis():
    while True:
        print(
            "\n1. Cadastrar hotel\n2. Cadastrar quarto\n3. Listar hotéis e quartos\n0. Voltar"
        )
        op = input("Opção: ").strip()
        if op == "1":
            cadastrar_hotel()
        elif op == "2":
            cadastrar_quarto()
        elif op == "3":
            listar_hoteis()
        elif op == "0":
            break
        else:
            print("Opção inválida.")
