class Meta:
    """
    Classe que representa uma meta a ser atingida.

    Atributos:
        tipo (str): O tipo da meta (ex: "Distância", "Tempo").
        distancia (float): A distância relacionada à meta.
        tempo (float, opcional): O tempo associado à meta, caso se trate de uma meta de tempo.
    """

    def __init__(self, tipo: str, distancia: float, tempo: float = -1) -> None:
        """
        Construtor da classe Meta.

        Argumentos:
            tipo (str): O tipo da meta (ex: "Distância", "Tempo").
            distancia (float): A distância relacionada à meta.
            tempo (float, opcional): O tempo associado à meta, caso se trate de uma meta de tempo.
        """
        self.tipo = tipo
        self.distancia = distancia
        self.tempo = tempo

    def __str__(self) -> str:
        """
        Retorna uma representação em string da meta.

        Retorna:
            str: Representação da meta no formato "tipo, distancia, tempo" (se tempo for fornecido).
        """
        return f"{self.tipo}, {self.distancia} km{f', {self.tempo}m' if self.tempo else ''}"
