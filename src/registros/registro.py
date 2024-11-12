from .. import data as Data


class Registro:
    """
    Classe para armazenar informações sobre um treino ou competição de corrida.

    A classe `Registro` guarda os detalhes de uma sessão de corrida,
    seja um treino ou uma competição.
    Os atributos incluem o tipo de atividade, data, distância, duração,
    localização e clima.

    Atributos:
        tipo (str): Indica se é um "treino" ou "competição".
        data (Data): Objeto `Data` representando a data do evento, no
        formato DD/MM/AA.
        distancia (int): Distância percorrida em quilômetros.
        duracao (int): Duração da sessão em minutos.
        localizacao (str): Local onde o evento ocorreu.
        clima (str): Condições climáticas durante o evento.

    Métodos:
        __init__(self, tipo: str, data: str, distancia: int, duracao: int,
        localizacao: str, clima: str) -> None:
            Inicializa uma nova instância da classe `Registro` com os detalhes
            especificados.

        __str__(self) -> str:
            Retorna uma string formatada representando os detalhes do registro
            de corrida.
    """

    def __init__(self, tipo: str, data: str, distancia: int, duracao: int,
                 localizacao: str, clima: str) -> None:
        """
        Inicializa uma nova instância de `Registro`.

        Args:
            tipo (str): Tipo de sessão, pode ser "treino" ou "competição".
            data (str): Data do evento, no formato DD/MM/AA.
            distancia (int): Distância percorrida, em quilômetros.
            duracao (int): Duração do evento, em minutos.
            localizacao (str): Local onde o evento ocorreu.
            clima (str): Condições climáticas durante o evento.
        """
        self.tipo: str = tipo
        self.data: Data.Data = Data.Data(data)
        self.distancia: int = distancia
        self.duracao: int = duracao
        self.localizacao: str = localizacao
        self.clima: str = clima

    def __str__(self):
        """
        Retorna uma representação em string do registro de corrida.

        Returns:
            str: String formatada contendo os detalhes da sessão de corrida.
        """
        return f"{self.tipo}, {self.data}, {self.distancia} km, {
            self.duracao
        } m, {self.localizacao}, {self.clima}"
