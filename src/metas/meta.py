class Meta:
    def __init__(self, tipo: str, distancia: float, tempo: float = None) -> None:
        self.tipo = tipo
        self.distancia = distancia
        self.tempo = tempo

    def __str__(self) -> str:
        return f"{self.tipo}, {self.distancia}{f", {self.tempo}" if self.tempo else ""}"
