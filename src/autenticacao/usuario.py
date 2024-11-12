class Usuario:
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"{self.nome}, {self.email}, {self.senha}"

