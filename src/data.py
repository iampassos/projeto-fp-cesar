from datetime import datetime


class Data:
    def __init__(self, data: str):
        dia, mes, ano = data.split("/")
        self.dia: int = int(dia)
        self.mes: int = int(mes)
        self.ano: int = int(ano)

    def data_atual() -> 'Data':
        data_hoje = datetime.now()
        ano, mes, dia = data_hoje.date().split("-")

        return Data(f"{dia:02}/{mes:02}/{ano:04}")

    def __str__(self) -> str:
        return f"{self.dia:02}/{self.mes:02}/{self.ano:04}"
