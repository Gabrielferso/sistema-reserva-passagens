class Hospedagem:
    def __init__(self, id_hospedagem, passageiro_id, hotel_id, quarto_id, entrada, saida, valor):
        self.id = id_hospedagem
        self.passageiro_id = passageiro_id
        self.hotel_id = hotel_id
        self.quarto_id = quarto_id
        self.entrada = entrada
        self.saida = saida
        self.valor = valor
        self.ativa = True

    def __str__(self):
        estado = "Ativa" if self.ativa else "Cancelada"
        return (f"Hospedagem {self.id} | Passageiro {self.passageiro_id} | Hotel {self.hotel_id} | "
                f"Quarto {self.quarto_id} | {self.entrada} a {self.saida} | R$ {self.valor:.2f} | {estado}")
