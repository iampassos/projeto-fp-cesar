from .. import ferramentas
from . import registro

registro_caminho = "registros.csv"


def adicionar_registro(caminho, dados):
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    atributos = ["tipo", "data", "distancia",
                 "duracao", "localizacao", "clima", ]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_registro = dados.__dict__.values()
    arquivo.append(novo_registro)

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)

    return novo_registro


def index_valido(index, arquivo):
    return index >= 0 and index < len(arquivo)


def ler_registro(caminho, index=None):
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index:
        return [registro.Registro(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    registro_lido = registro.Registro(*arquivo[index])

    return registro_lido


def atualizar_registro(caminho, index, dados):
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)


def deletar_registro(caminho, index):
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)


