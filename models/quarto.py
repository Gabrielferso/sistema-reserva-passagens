class Quarto:
    def __init__(self, id_quarto, numero, capacidade, diaria):
        self.id = id_quarto
        self.numero = numero
        self.capacidade = capacidade
        self.diaria = diaria

    def __str__(self):
        return f"Quarto {self.id} | Nº {self.numero} | Capacidade: {self.capacidade} | Diária: R$ {self.diaria:.2f}"
