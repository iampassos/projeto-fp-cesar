from datetime import datetime
from ..registros import funcionalidades


def acompanhar_meta(dados, meta):
    filtrados = funcionalidades.registros_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    if meta.tempo:
        resultados = []

        for i in filtrados:
            tempo = (i.distancia / i.duracao) * 60
            resultados.append(tempo >= (meta.quantidade / meta.tempo) * 60)

        return resultados

    soma = 0

    for i in filtrados:
        soma += i.distancia

    return soma




