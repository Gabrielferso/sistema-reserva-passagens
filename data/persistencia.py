
from data import banco
from data.arquivo import salvar_dados, carregar_dados
from models.passageiro import Passageiro
from models.voo import Voo
from models.reserva import Reserva
from models.hotel import Hotel
from models.quarto import Quarto
from models.hospedagem import Hospedagem
from models.pacote import Pacote


def salvar_banco():
    salvar_dados("passageiros.txt", [
        [p.id, p.nome, p.documento, p.telefone, p.email]
        for p in banco.passageiros
    ])

    salvar_dados("voos.txt", [
        [v.id, v.origem, v.destino, v.data, v.horario,
         v.aeronave, v.capacidade]
        for v in banco.voos
    ])

    salvar_dados("reservas.txt", [
        [r.id, r.passageiro_id, r.voo_id, r.assento,
         r.valor, r.ativa]
        for r in banco.reservas
    ])

    salvar_dados("hoteis.txt", [
        [h.id, h.nome, h.cidade]
        for h in banco.hoteis
    ])

    salvar_dados("quartos.txt", [
        [h.id, q.id, q.numero, q.capacidade, q.diaria]
        for h in banco.hoteis
        for q in h.quartos
    ])

    salvar_dados("hospedagens.txt", [
        [h.id, h.passageiro_id, h.hotel_id, h.quarto_id,
         h.entrada, h.saida, h.valor, h.ativa]
        for h in banco.hospedagens
    ])

    salvar_dados("pacotes.txt", [
        [p.id, p.reserva_id, p.hospedagem_id,
         p.valor, p.ativo]
        for p in banco.pacotes
    ])


def carregar_banco():
    banco.passageiros.clear()
    banco.voos.clear()
    banco.reservas.clear()
    banco.hoteis.clear()
    banco.hospedagens.clear()
    banco.pacotes.clear()

    for r in carregar_dados("passageiros.txt"):
        banco.passageiros.append(
            Passageiro(int(r[0]), r[1], r[2], r[3], r[4])
        )

    for r in carregar_dados("voos.txt"):
        banco.voos.append(
            Voo(int(r[0]), r[1], r[2], r[3], r[4], r[5], int(r[6]))
        )

    for r in carregar_dados("reservas.txt"):
        reserva = Reserva(
            int(r[0]), int(r[1]), int(r[2]), r[3], float(r[4])
        )
        reserva.ativa = r[5] == "True"
        banco.reservas.append(reserva)

    for r in carregar_dados("hoteis.txt"):
        banco.hoteis.append(Hotel(int(r[0]), r[1], r[2]))

    for r in carregar_dados("quartos.txt"):
        hotel_id = int(r[0])
        quarto = Quarto(int(r[1]), r[2], int(r[3]), float(r[4]))

        for hotel in banco.hoteis:
            if hotel.id == hotel_id:
                hotel.quartos.append(quarto)
                break

    for r in carregar_dados("hospedagens.txt"):
        hospedagem = Hospedagem(
            int(r[0]), int(r[1]), int(r[2]), int(r[3]),
            r[4], r[5], float(r[6])
        )
        hospedagem.ativa = r[7] == "True"
        banco.hospedagens.append(hospedagem)

    for r in carregar_dados("pacotes.txt"):
        pacote = Pacote(
            int(r[0]), int(r[1]), int(r[2]), float(r[3])
        )
        pacote.ativo = r[4] == "True"
        banco.pacotes.append(pacote)

    atualizar_contadores()


def atualizar_contadores():
    entidades = {
        "passageiro": banco.passageiros,
        "voo": banco.voos,
        "reserva": banco.reservas,
        "hotel": banco.hoteis,
        "quarto": [
            quarto
            for hotel in banco.hoteis
            for quarto in hotel.quartos
        ],
        "hospedagem": banco.hospedagens,
        "pacote": banco.pacotes
    }

    for tipo, registros in entidades.items():
        ids = [registro.id for registro in registros]
        banco.contadores[tipo] = max(ids, default=0) + 1
