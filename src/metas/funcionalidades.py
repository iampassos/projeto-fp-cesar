from datetime import datetime
from ..registros import funcionalidades


def acompanhar_meta_distancia(dados, meta):
    filtrados = funcionalidades.filtrar_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    total = sum([i.distancia for i in filtrados])

    return total


def acompanhar_meta_tempo(dados, meta):
    filtrados = funcionalidades.filtrar_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    resultados = []

    for i in filtrados:
        tempo = (i.distancia / i.duracao) * 60
        resultados.append([i, tempo >= (meta.distancia / meta.tempo) * 60])

    return resultados

