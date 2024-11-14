from datetime import datetime
from ..registros import funcionalidades
from .meta import Meta
from ..registros.registro import Registro


def acompanhar_meta_distancia(dados: list[Registro], meta: Meta) -> [int, float]:
    filtrados = funcionalidades.filtrar_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    total = sum([float(i.distancia) for i in filtrados])

    return [len(filtrados), total / float(meta.distancia)]


def acompanhar_meta_tempo(dados: list[Registro], meta: Meta) -> list[list[Registro, bool]]:
    filtrados = funcionalidades.filtrar_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    resultados = []

    for i in filtrados:
        tempo = (float(i.distancia) / float(i.duracao)) * 60
        resultados.append(
            [i, tempo >= (float(meta.distancia) / float(meta.tempo)) * 60])

    return resultados
