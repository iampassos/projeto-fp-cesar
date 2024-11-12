from ..data import Data


class Registro:
    def __init__(self, tipo: str, data, distancia: float, duracao: float, localizacao: str, clima: str):
        self.tipo = tipo
        self.data = Data(data)
        self.distancia = distancia
        self.duracao = duracao
        self.localizacao = localizacao
        self.clima = clima

    def __str__(self) -> str:
        return f"{self.tipo}, {self.data}, {self.distancia}, {self.duracao}, {self.localizacao}, {self.clima}"
