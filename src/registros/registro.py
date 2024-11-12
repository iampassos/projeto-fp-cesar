from .. import data as Data


class Registro:
    def __init__(
        self,
        tipo: str,
        data: str,
        distancia: int,
        duracao: int,
        localizacao: str,
        clima: str,
    ) -> None:
        self.tipo: str = tipo
        self.data: Data.Data = Data.Data(data)
        self.distancia: int = distancia
        self.duracao: int = duracao
        self.localizacao: str = localizacao
        self.clima: str = clima

    def __str__(self):
        return f"{self.tipo}, {self.data}, {self.distancia} km, {self.duracao} m, {self.localizacao}, {self.clima}"
