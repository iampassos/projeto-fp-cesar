# Lista para salvar os treinos

treino_data = []

# Dicionário com os índices de cada informação por coluna na matriz

index = {
    "tipo": 0,
    "data": 1,
    "distancia": 2,
    "duracao": 3,
    "localizacao": 4,
    "clima": 5,
}

# Meta de distância no mês

meta_distancia_mes = 0

# Definindo uma tupla para armazenar uma data

def Data(dia, mes, ano):
    return (dia, mes, ano)

# Adiciona um treino na lista de treinos

def add_treino(tipo, data, distancia, duracao, localizacao, clima):
    global treino_data
    treino_data.append([tipo, data, distancia, duracao, localizacao, clima])

# Define uma nova meta de distância por mês

def nova_meta(meta):
    global meta_distancia_mes
    meta_distancia_mes = meta

# Filtra um treino por um critério específico
# Ao colocar a variável modo como: "distancia" o método filtra os elementos pela distância
# Ao colocar a variável modo como: "duracao" o método filtra os elementos pela duração

def filtrar(modo, data):
    indice = index[modo]
    treino_filtrado = []
    global treino_data
    for treino in treino_data:
        if treino[indice] == data:
            treino_filtrado.append(treino)
    
    return treino_filtrado

# Função que ordena a lista pelas datas
def ordenar_data():
    def ord_func(treino):
        data = treino[index["data"]]
        dia = data[0]
        mes = data[1]
        ano = data[2]

        return dia + mes * 30.416 + ano * 365.25
    
    global treino_data
    treinos_ordenados = sorted(treino_data, key=lambda treino: ord_func(treino))

    return treinos_ordenados

add_treino("competição", (8, 10, 2024), 100, 40, "Recife", "Chuvoso")
add_treino("competição", (2, 11, 2024), 90, 35, "Recife", "Chuvoso")
add_treino("competição", (24, 9, 2024), 20, 10, "Recife", "Chuvoso")

print(ordenar_data())