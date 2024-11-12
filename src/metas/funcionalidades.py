from ..registros import registro as Registro


def distancia_mes(dados: list[Registro.Registro], mes: int):
    filtrados = []

    for i in dados:
        print(i)
        if i.data.mes == mes:
            filtrados.append(i)

    return filtrados


distancia_mes(
    [
        Registro.Registro("treino", "12/11/24", 100,
                          100, "recife", "agradavel"),
        Registro.Registro("treino", "12/11/24", 100,
                          100, "recife", "agradavel"),
        Registro.Registro("treino", "12/11/24", 100,
                          100, "recife", "agradavel"),
        Registro.Registro("treino", "12/11/24", 100,
                          100, "recife", "agradavel"),
        Registro.Registro("treino", "12/11/24", 100,
                          100, "recife", "agradavel"),
    ]
)
