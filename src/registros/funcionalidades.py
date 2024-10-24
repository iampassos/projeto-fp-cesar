import random
from .. import ferramentas

# Dicionário com os índices de cada informação por coluna na matriz

index = {
    "tipo": 0,
    "data": 1,
    "distancia": 2,
    "duracao": 3,
    "localizacao": 4,
    "clima": 5,
}


# Filtra os registros por um critério específico
# O modo filtra pelas colunas (tipo, data, distancia, etc)

def filtrar(dados, modo, data):
    indice = index[modo]
    registros_filtrados = []

    for registro in dados:
        if registro[indice] == data:
            registros_filtrados.append(registro)

    return registros_filtrados


# Função que ordena os dados pelas datas


def ordenar_data(dados):
    def ordenar(registro):
        data = registro[index["data"]]
        dia = data[0]
        mes = data[1]
        ano = data[2]

        return dia + mes * 31 + ano * 372

    registros_ordenados = sorted(
        dados, key=lambda registro: ordenar(registro))

    return registros_ordenados


# Função que sugere um treino novo seguindo
# a média de distância e tempo do usuário


def sugerir_treino(dados):
    media_dist = 0
    media_tempo = 0

    total = len(dados)

    for registro in dados:
        media_dist += registro[index["distancia"]] / total
        media_tempo += registro[index["duracao"]] / total

    delta_dist = int(media_dist / 5)
    delta_tempo = int(media_tempo / 5)

    std_dist = random.randint(-delta_dist, delta_dist)
    std_tempo = random.randint(-delta_tempo, delta_tempo)

    return ["treino", ferramentas.data(8, 10, 2024),
            int(media_dist + std_dist), int(media_tempo + std_tempo),
            "Recife", "Aberto"]
