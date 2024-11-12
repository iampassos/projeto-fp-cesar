from .. import ferramentas
from . import meta as Meta

metas_caminho: str = "./data/metas.csv"


def adicionar_meta(dados: Meta.Meta) -> list[str]:
    arquivo: list[list[str]] = ferramentas.ler_csv(metas_caminho)

    atributos: list[str] = ["tipo, descricao", "quantidade"]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_meta: list[str] = dados.__str__().split(", ")
    arquivo.append(novo_meta)

    ferramentas.escrever_csv(metas_caminho, arquivo)

    return novo_meta


def index_valido(index: int, arquivo: list[list[str]]) -> bool:
    return index >= 0 and index < len(arquivo)


def ler_meta(index: int = None) -> Meta.Meta | list[Meta.Meta] | None:
    arquivo: list[list[str]] = ferramentas.ler_csv(metas_caminho)

    if not index:
        return [Meta(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    meta: Meta = Meta(*arquivo[index])

    return meta


def atualizar_meta(index: int, dados: Meta) -> None:
    arquivo: list[list[str]] = ferramentas.ler_csv(metas_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(metas_caminho, arquivo)


def deletar_meta(index: int) -> None:
    arquivo: list[list[str]] = ferramentas.ler_csv(metas_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(metas_caminho, arquivo)
