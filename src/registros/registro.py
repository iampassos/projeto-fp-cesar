# Essa classe reune todos os dados que um registro precisa,
# com o intuito de criar uma "receita" para acessar os dados

class Registro:
    def __init__(self, tipo, data, distancia, duracao, localizacao, clima):
        self.tipo = tipo
        self.data = data
        self.distancia = distancia
        self.duracao = duracao
        self.localizacao = localizacao
        self.clima = clima

