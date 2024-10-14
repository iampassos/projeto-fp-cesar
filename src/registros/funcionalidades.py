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
    registrosFiltrados = []

    for registro in dados:
        if registro[indice] == data:
            registrosFiltrados.append(registro)

    return registrosFiltrados


# Função que ordena os dados pelas datas


def ordenarData(dados):
    def ordenar(registro):
        data = registro[index["data"]]
        dia = data[0]
        mes = data[1]
        ano = data[2]

        return dia + mes * 31 + ano * 372

    registrosOrdenados = sorted(
        dados, key=lambda registro: ordenar(registro))

    return registrosOrdenados


# Função que sugere um treino novo seguindo
# a média de distância e tempo do usuário


def sugerirTreino(dados):
    mediaDist = 0
    mediaTempo = 0

    total = len(dados)

    for registro in dados:
        mediaDist += registro[index["distancia"]] / total
        mediaTempo += registro[index["duracao"]] / total

    deltaDist = int(mediaDist / 5)
    deltaTempo = int(mediaTempo / 5)

    stdDist = random.randint(-deltaDist, deltaDist)
    stdTempo = random.randint(-deltaTempo, deltaTempo)

    return ["treino", ferramentas.data(8, 10, 2024),
            int(mediaDist + stdDist), int(mediaTempo + stdTempo),
            "Recife", "Aberto"]
