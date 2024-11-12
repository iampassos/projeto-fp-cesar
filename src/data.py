class Data:
    def __init__(self, dataStr: str) -> None:
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
        return f"{self.dia:02}/{self.mes:02}/{self.ano:04}"
