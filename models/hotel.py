class Hotel:
    def __init__(self, id_hotel, nome, cidade):
        self.id = id_hotel
        self.nome = nome
        self.cidade = cidade
        self.quartos = []

    def __str__(self):
        return f"Hotel {self.id} | {self.nome} | {self.cidade} | Quartos cadastrados: {len(self.quartos)}"
