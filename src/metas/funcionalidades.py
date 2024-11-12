from datetime import datetime
from ..registros import registro as Registro
from ..registros import funcionalidades
from . import meta as Meta


def acompanhar_meta_distancia(dados: list[Registro.Registro], meta: Meta.Meta):
    filtrados = funcionalidades.registros_mes(dados, datetime.now().month)

    soma = 0

    for i in filtrados:
        soma += i.distancia

    return soma


def acompanhar_meta_tempo(dados: list[Registro.Registro], meta: Meta.Meta):
    filtrados = funcionalidades.registros_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    resultados = []

    for i in filtrados:
        tempo = (i.distancia / i.duracao) * 60
        resultados.append(tempo >= (meta.quantidade / meta.tempo) * 60)

    return resultados

