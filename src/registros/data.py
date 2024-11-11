class Data:
    """
    Armazena uma data -> dia/mes/ano
    """
    def __init__(self, dataStr: str) -> None:
        """
        Argumentos:

            dataStr: String contendo o conteúdo da data "DD/MM/AA"

        Salva o dia, mês e ano em valores inteiros.
        """
        dia, mes, ano = dataStr.split("/")

        self.dia: int = int(dia)
        self.mes: int = int(mes)
        self.ano: int = int(ano)

    def __str__(self) -> str:
        """
        Retorna uma string com a data formatada "DD/MM/AA"
        """
        return f"{self.dia:02}/{self.mes:02}/{self.ano}"
