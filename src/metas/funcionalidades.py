from datetime import datetime
from ..registros import funcionalidades
from .meta import Meta


def acompanhar_meta_distancia(dados: list[Meta], meta: Meta) -> float:
    """
    Acompanha a meta de distância, somando todas as distâncias realizadas no mês atual.

    Argumentos:
        dados (list[Meta]): Lista de metas contendo os dados de distâncias.
        meta (Meta): A meta a ser acompanhada.

    Retorna:
        float: O total de distância acumulado no mês atual.

    Exemplo de uso:
        acompanhar_meta_distancia(dados, meta_exemplo)
    """
    filtrados = funcionalidades.filtrar_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    total = sum([i.distancia for i in filtrados])

    return total


def acompanhar_meta_tempo(dados: list[Meta], meta: Meta) -> list[list[Meta, bool]]:
    """
    Acompanha a meta de tempo, verificando se o tempo gasto para cada meta de distância foi suficiente.

    Argumentos:
        dados (list[Meta]): Lista de metas contendo as distâncias e tempos realizados.
        meta (Meta): A meta a ser acompanhada.

    Retorna:
        list[list[Meta, bool]]: Uma lista contendo metas e um valor booleano indicando se o tempo 
        foi atingido para cada meta.

    Exemplo de uso:
        acompanhar_meta_tempo(dados, meta_exemplo)
    """
    filtrados = funcionalidades.filtrar_mes(
        dados, datetime.now().month, datetime.now().year % 100)

    resultados = []

    for i in filtrados:
        tempo = (i.distancia / i.duracao) * 60
        resultados.append([i, tempo >= (meta.distancia / meta.tempo) * 60])

    return resultados
