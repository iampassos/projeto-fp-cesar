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

registroCaminho = "./data/registros.csv"


# Adicionar um registro ao banco de dados


def adicionarRegistro(dados):
    arquivo = ferramentas.lerCSV(registroCaminho)

    if len(arquivo) == 0:
        arquivo.append(["tipo", "data", "distancia",
                        "duracao", "localizacao", "clima"])

    novoRegistro = ",".join(str(valor) for valor in dados.values()).split(",")
    arquivo.append(novoRegistro)

    ferramentas.escreverCSV(registroCaminho, arquivo)


# Ler um registro do banco de dados baseado no índice (começa no 1)


def lerRegistro(index=None):
    arquivo = ferramentas.lerCSV(registroCaminho)

    if not index:
        return arquivo

    if index >= len(arquivo) or index < 0:
        return None

    return arquivo[index]


# Atualizar um registro do banco de dados
# a partir do índice (começa no 1)
# Obs: dados são uma LISTA com os dados em ordem
# atualizarRegistro(0, ["", "", etc..])


def atualizarRegistro(index, dados):
    registro = lerRegistro(index)

    if not registro:
        return None

    arquivo = ferramentas.lerCSV(registroCaminho)
    arquivo[index] = dados

    ferramentas.escreverCSV(registroCaminho, arquivo)

    return dados


# Remover um registro do banco de dados
# baseado no índice (começa no 1)


def removerRegistro(index):
    registro = lerRegistro(index)

    if not registro:
        return

    arquivo = ferramentas.lerCSV(registroCaminho)
    arquivo.pop(index)

    ferramentas.escreverCSV(registroCaminho, arquivo)

