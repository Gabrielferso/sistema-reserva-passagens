class Passageiro:
    def __init__(self, id_passageiro, nome, documento, telefone, email):
        self.id = id_passageiro
        self.nome = nome
        self.documento = documento
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"ID {self.id} | {self.nome} | Documento: {self.documento} | Telefone: {self.telefone} | E-mail: {self.email}"
