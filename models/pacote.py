class Pacote:
    def __init__(self, id_pacote, reserva_id, hospedagem_id, valor):
        self.id = id_pacote
        self.reserva_id = reserva_id
        self.hospedagem_id = hospedagem_id
        self.valor = valor
        self.ativo = True

    def __str__(self):
        estado = "Ativo" if self.ativo else "Cancelado"
        return f"Pacote {self.id} | Reserva {self.reserva_id} | Hospedagem {self.hospedagem_id} | R$ {self.valor:.2f} | {estado}"
