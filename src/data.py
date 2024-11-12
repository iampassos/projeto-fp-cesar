class Data:
    """
    Classe para armazenar uma data no formato dia/mês/ano.

    A classe `Data` permite representar uma data a partir de uma string no
    formato "DD/MM/AA" e
    fornece métodos para acessar e exibir essa data de maneira formatada.

    Atributos:
        dia (int): Dia do mês.
        mes (int): Mês do ano.
        ano (int): Ano (no formato de dois dígitos).

    Métodos:
        __init__(self, dataStr: str) -> None:
            Inicializa uma instância da classe `Data` a partir de uma string
            de data.

        __str__(self) -> str:
            Retorna a data formatada como uma string no formato "DD/MM/AA".
    """

    def __init__(self, dataStr: str) -> None:
        """
        Inicializa uma instância de `Data` a partir de uma string no formato
        "DD/MM/AA".

        Argumentos:
            dataStr (str): String contendo a data no formato "DD/MM/AA".

        Atribui os valores de dia, mês e ano como inteiros.
        """
        dia, mes, ano = dataStr.split("/")
        self.dia: int = int(dia)
        self.mes: int = int(mes)
        self.ano: int = int(ano)

    @staticmethod
    def data_atual():
        from datetime import datetime

        # Obtendo a data e hora atual
        data_hoje = datetime.now()

        # Exibindo apenas a data (sem a hora)
        ano, mes, dia = data_hoje.date().split("-")

        return Data(f"{dia:02}/{mes:02}/{ano:04}")

    def __str__(self) -> str:
        """
        Retorna uma representação em string da data no formato "DD/MM/AA".

        Returns:
            str: Data formatada como "DD/MM/AA".
        """
        return f"{self.dia:02}/{self.mes:02}/{self.ano:04}"
