import random
from . import registro as Registro
from .. import data as Data


def filtrar(dados: list[Registro], modo: str, valor) -> list[Registro]:
    registros_filtrados: list[Registro] = []

    for registro in dados:
        if getattr(registro, modo) == valor:
            registros_filtrados.append(registro)

    return registros_filtrados


def filtrar_mes(dados: list[Registro.Registro], mes: int, ano: int):
    filtrados = []

    for i in dados:
        if i.data.mes == mes and i.data.ano == ano:
            filtrados.append(i)

    return filtrados


def ordenar_data(dados: list[Registro]) -> list[Registro]:
    def ordenar(registro: Registro) -> int:
        data = registro.data  # Assumindo que `data` é um objeto `Data`
        dia = data.dia
        mes = data.mes
        ano = data.ano

        return dia + mes * 31 + ano * 372

    registros_ordenados: list[Registro] = sorted(dados, key=ordenar)

    return registros_ordenados


def sugerir_treino(dados: list[dict]) -> Registro:
    media_dist = 0
    media_tempo = 0

    total = len(dados)

    # Cálculo das médias de distância e duração
    for registro in dados:
        media_dist += registro["distancia"]
        media_tempo += registro["duracao"]

    # Calculando as médias
    media_dist /= total
    media_tempo /= total

    # Calculando os deltas de variação para distâncias e durações
    delta_dist = int(media_dist / 5)
    delta_tempo = int(media_tempo / 5)

    # Gerando uma variação aleatória para a distância e duração sugeridas
    std_dist = random.randint(-delta_dist, delta_dist)
    std_tempo = random.randint(-delta_tempo, delta_tempo)

    # Retornando o treino sugerido
    return Registro(
        "treino",
        Data.data_atual(),
        int(media_dist + std_dist),  # Distância sugerida ajustada
        int(media_tempo + std_tempo),  # Duração sugerida ajustada
        "Recife",  # Local do treino
        "Aberto",  # Clima do treino
    )
