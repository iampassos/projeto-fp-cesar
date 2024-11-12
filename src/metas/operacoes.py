from .. import ferramentas
from . import meta

metas_caminho = "metas.csv"


def adicionar_meta(caminho, dados):
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    atributos = ["tipo", "descricao", "quantidade"]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_meta = dados.__str__().split(", ")
    arquivo.append(novo_meta)

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)

    return novo_meta


def index_valido(index, arquivo):
    return index >= 0 and index < len(arquivo)


def ler_meta(caminho, index=None):
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index:
        return [meta.Meta(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    meta_lida = meta.Meta(*arquivo[index])

    return meta_lida


def atualizar_meta(caminho, index, dados):
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)


def deletar_meta(caminho, index):
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)

