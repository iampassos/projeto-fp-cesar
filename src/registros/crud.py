from .. import ferramentas


# Formato geral de respostas: (A ordem importa)
# {
#     "tipo": "",
#     "data": "",
#     "distancia": "",
#     "duracao": "",
#     "localizacao": "",
#     "clima": "",
# }
# Em algumas funções, será retornado uma LISTA ou None

treinoCaminho = "./data/treinos.csv"


# Adicionar um treino/competição ao banco de dados


def addTreino(dados):
    arquivo = ferramentas.lerCSV(treinoCaminho)

    arquivo[0] = ["tipo", "data", "distancia",
                  "duracao", "localizacao", "clima"]

    novoTreino = ",".join(str(valor) for valor in dados.values()).split(",")
    arquivo.append(novoTreino)

    ferramentas.escreverCSV(treinoCaminho, arquivo)


# Ler um treino/competição do banco de dados baseado no índice (começa no 1)


def lerTreino(index=None):
    arquivo = ferramentas.lerCSV(treinoCaminho)

    if not index:
        return arquivo

    if index >= len(arquivo) or index < 0:
        return None

    return arquivo[index]


# Atualizar um treino/competição do banco de dados
# a partir do índice (começa no 1)
# Obs: dados são uma LISTA com os dados em ordem
# atualizarTreino(0, ["", "", etc..])


def atualizarTreino(index, dados):
    treino = lerTreino(index)

    if not treino:
        return None

    arquivo = ferramentas.lerCSV(treinoCaminho)
    arquivo[index] = dados

    ferramentas.escreverCSV(treinoCaminho, arquivo)

    return dados


# Remover um treino/competição do banco de dados
# baseado no índice (começa no 1)


def removerTreino(index):
    treino = lerTreino(index)

    if not treino:
        return

    arquivo = ferramentas.lerCSV(treinoCaminho)
    arquivo.pop(index)

    ferramentas.escreverCSV(treinoCaminho, arquivo)

