class Reserva:
    def __init__(self, id_reserva, passageiro_id, voo_id, assento, valor):
        self.id = id_reserva
        self.passageiro_id = passageiro_id
        self.voo_id = voo_id
        self.assento = assento
        self.valor = valor
        self.ativa = True

    def __str__(self):
        estado = "Ativa" if self.ativa else "Cancelada"
        return (f"Reserva {self.id} | Passageiro {self.passageiro_id} | Voo {self.voo_id} | "
                f"Assento {self.assento} | R$ {self.valor:.2f} | {estado}")
