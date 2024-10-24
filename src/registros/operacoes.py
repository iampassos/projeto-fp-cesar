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

registro_caminho = "./data/registros.csv"


# Adicionar um registro ao banco de dados


def adicionar_registro(dados):
    arquivo = ferramentas.ler_csv(registro_caminho)

    if len(arquivo) == 0:
        arquivo.append(["tipo", "data", "distancia",
                        "duracao", "localizacao", "clima"])

    novo_registro = [str(valor) for valor in dados.values()]
    arquivo.append(novo_registro)

    ferramentas.escrever_csv(registro_caminho, arquivo)

    return novo_registro


# Ler um registro do banco de dados baseado no índice (começa no 1)


def ler_registro(index=None):
    arquivo = ferramentas.ler_csv(registro_caminho)

    if not index:
        return arquivo

    if index >= len(arquivo) or index < 0:
        return None

    return arquivo[index]


# Atualizar um registro do banco de dados
# a partir do índice (começa no 1)
# Obs: dados são uma LISTA com os dados em ordem
# atualizar_registro(0, ["", "", etc..])


def atualizar_registro(index, dados):
    registro = ler_registro(index)

    if not registro:
        return None

    arquivo = ferramentas.ler_csv(registro_caminho)
    arquivo[index] = dados

    ferramentas.escrever_csv(registro_caminho, arquivo)

    return dados


# Deletar um registro do banco de dados
# baseado no índice (começa no 1)


def deletar_registro(index):
    registro = ler_registro(index)

    if not registro:
        return

    arquivo = ferramentas.ler_csv(registro_caminho)
    arquivo.pop(index)

    ferramentas.escrever_csv(registro_caminho, arquivo)

