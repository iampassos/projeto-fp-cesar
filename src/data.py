from datetime import datetime


class Data:
    """
    Classe que representa uma data no formato DD/MM/AAAA.

    Atributos:
        dia (int): O dia da data.
        mes (int): O mês da data.
        ano (int): O ano da data.
    """

    def __init__(self, data: str):
        """
        Construtor da classe Data.

        Argumento:
            data (str): A data no formato "DD/MM/AAAA".
        """
        dia, mes, ano = data.split("/")
        self.dia: int = int(dia)
        self.mes: int = int(mes)
        self.ano: int = int(ano)

    def data_atual() -> 'Data':
        """
        Retorna a data atual no formato "DD/MM/AAAA".

        Retorna:
            Data: A data de hoje.

        Exemplo de uso:
            data_hoje = Data.data_atual()
        """

        data_hoje = datetime.now()
        dia, mes, ano = data_hoje.strftime("%d-%m-%Y").split("-")

        return Data(f"{dia}/{mes}/{ano}")


def __str__(self) -> str:
    """
        Retorna a representação da data como uma string no formato "DD/MM/AAAA".

        Retorna:
            str: A data representada como string.

        Exemplo de uso:
            str(data_obj)
        """
    return f"{self.dia:02}/{self.mes:02}/{self.ano:04}"
