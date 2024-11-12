class Meta:
    def __init__(self, tipo: str, descricao: str, quantidade: int) -> None:
        self.tipo = tipo
        self.descricao = descricao
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.tipo}, {self.descricao}, {self.quantidade}"
