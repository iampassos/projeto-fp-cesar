from datetime import datetime
from ..registros import registro as Registro
from . import meta as Meta


def registros_mes(dados: list[Registro.Registro], mes: int, ano: int):
    filtrados = []

    for i in dados:
        if i.data.mes == mes and i.data.ano == ano:
            filtrados.append(i)

    return filtrados


def acompanhar_meta_distancia(dados: list[Registro.Registro], meta: Meta.Meta):
    filtrados = registros_mes(dados, datetime.now().month)

    soma = 0

    for i in filtrados:
        soma += i.distancia

    return soma


def acompanhar_meta_tempo(dados: list[Registro.Registro], meta: Meta.Meta):
    filtrados = registros_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    resultados = []

    for i in filtrados:
        tempo = (i.distancia / i.duracao) * 60
        resultados.append(tempo >= (meta.quantidade / meta.tempo) * 60)

    return resultados


print(acompanhar_meta_tempo(
    [
        Registro.Registro("treino", "12/11/21", 80,
                          20, "recife", "agradavel"),
        Registro.Registro("treino", "12/11/21", 2,
                          120, "recife", "agradavel"),
        Registro.Registro("treino", "12/11/22", 10,
                          60, "recife", "agradavel"),
        Registro.Registro("treino", "12/10/22", 4.9,
                          60, "recife", "agradavel"),
    ],
    Meta.Meta("tempo", "Melhorar tempo em 5km/h", 5, 60)
))
