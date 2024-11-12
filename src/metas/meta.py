class Meta:
    def __init__(self, tipo: str, descricao: str, quantidade: int,
                 tempo=None) -> None:
        self.tipo = tipo
        self.descricao = descricao
        self.quantidade = quantidade
        self.tempo = tempo

    def __str__(self):
        return f"{self.tipo}, {self.descricao}, {self.quantidade}"