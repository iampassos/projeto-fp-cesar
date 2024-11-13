class Registro:
    """
    Classe que representa um registro de atividade.

    Atributos:
        tipo (str): O tipo de atividade (ex: caminhada, corrida).
        data (Data): A data do registro da atividade.
        distancia (float): A distância percorrida na atividade.
        duracao (float): A duração da atividade em minutos.
        localizacao (str): A localização onde a atividade foi realizada.
        clima (str): As condições climáticas durante a atividade.
    """

    def __init__(self, tipo: str, data: str, distancia: float, duracao: float, localizacao: str, clima: str):
        """
        Construtor da classe Registro.

        Argumentos:
            tipo (str): O tipo de atividade (ex: caminhada, corrida).
            data (str): A data do registro da atividade no formato "DD/MM/AAAA".
            distancia (float): A distância percorrida na atividade.
            duracao (float): A duração da atividade em minutos.
            localizacao (str): A localização onde a atividade foi realizada.
            clima (str): As condições climáticas durante a atividade.
        """
        self.tipo = tipo
        self.data = data
        self.distancia = distancia
        self.duracao = duracao
        self.localizacao = localizacao
        self.clima = clima

    def __str__(self) -> str:
        """
        Retorna uma representação da classe Registro como string.

        Retorna:
            str: A representação da atividade.

        Exemplo de uso:
            str(registro_obj)
        """
        return f"{self.tipo.capitalize()}, {self.data}, {self.distancia} km, {self.duracao}m, {self.localizacao.capitalize()}, {self.clima.capitalize()}"
