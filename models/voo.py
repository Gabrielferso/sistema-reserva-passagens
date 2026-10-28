class Voo:
    def __init__(self, id_voo, origem, destino, data, horario, aeronave, capacidade):
        self.id = id_voo
        self.origem = origem
        self.destino = destino
        self.data = data
        self.horario = horario
        self.aeronave = aeronave
        self.capacidade = capacidade

    def __str__(self):
        return (f"ID {self.id} | {self.origem} -> {self.destino} | "
                f"{self.data} às {self.horario} | Aeronave: {self.aeronave} | "
                f"Capacidade: {self.capacidade}")
