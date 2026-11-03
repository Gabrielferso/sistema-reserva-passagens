voos = []
reservas = []
hoteis = []
hospedagens = []
pacotes = []

contadores = {
    "passageiro": 1, "voo": 1, "reserva": 1,
    "hotel": 1, "quarto": 1, "hospedagem": 1, "pacote": 1
}

def novo_id(tipo):
    valor = contadores[tipo]
    contadores[tipo] += 1
    return valor
