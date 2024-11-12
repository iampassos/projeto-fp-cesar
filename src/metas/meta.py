class Meta:
    def __init__(self, tipo, distancia, tempo=None):
        self.tipo = tipo
        self.distancia = distancia
        self.tempo = tempo

    def __str__(self):
        return f"{self.tipo}, {self.distancia}{f", {self.tempo}" if self.tempo
                                               else ""}"
