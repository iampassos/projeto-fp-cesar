from datetime import datetime


class Data:
    def __init__(self, dataStr):
        dia, mes, ano = dataStr.split("/")
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)

    def data_atual():
        data_hoje = datetime.now()
        ano, mes, dia = data_hoje.date().split("-")

        return Data(f"{dia:02}/{mes:02}/{ano:04}")

    def __str__(self):
        return f"{self.dia:02}/{self.mes:02}/{self.ano:04}"
