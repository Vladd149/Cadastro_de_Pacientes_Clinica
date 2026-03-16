#classe paciente
class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __repr__(self):
        return f"Paciente(nome='{self.nome}', idade={self.idade})"