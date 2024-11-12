from .. import data as Data


class Registro:
    def __init__(self, tipo, data, distancia, duracao, localizacao, clima):
        self.tipo = tipo
        self.data = Data.Data(data)
        self.distancia = distancia
        self.duracao = duracao
        self.localizacao = localizacao
        self.clima = clima

    def __str__(self):
        return f"{self.tipo}, {self.data}, {
            self.distancia}, {self.duracao}, {
            self.localizacao}, {self.clima}"
