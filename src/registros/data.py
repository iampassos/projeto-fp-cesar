class Data:
    def __init__(self, str):
        dia, mes, ano = str.split("/")

        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)

    def __str__(self):
        return f"{self.dia:02}/{self.mes:02}/{self.ano}"