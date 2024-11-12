from .. import ferramentas
from .meta import Meta

metas_caminho = "metas.csv"


def adicionar_meta(caminho: str, dados: Meta) -> Meta:
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    atributos = ["tipo", "distancia", "tempo"]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    nova_meta = dados.__str__().split(", ")
    arquivo.append(nova_meta)

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)

    return Meta(*nova_meta)


def index_valido(index: int, arquivo: list) -> bool:
    return index >= 0 and index < len(arquivo)


def ler_meta(caminho: str, index: int = None) -> Meta | list[Meta] | None:
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index:
        return [Meta(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    return Meta(*arquivo[index])


def atualizar_meta(caminho: str, index: int, dados: Meta) -> None:
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)


def deletar_meta(caminho: str, index: int) -> None:
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)
