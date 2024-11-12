from .. import ferramentas
from .registro import Registro

registro_caminho = "registros.csv"


def adicionar_registro(caminho: str, dados: Registro) -> Registro:
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    atributos = ["tipo", "data", "distancia",
                 "duracao", "localizacao", "clima", ]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_registro = list(dados.__dict__.values())
    arquivo.append(novo_registro)

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)

    return novo_registro


def index_valido(index: int, arquivo: list) -> bool:
    return index >= 1 and index < len(arquivo)


def ler_registro(caminho: str, index: int = None) -> Registro | list[Registro] | None:
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index:
        return [Registro(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    registro_lido = Registro(*arquivo[index])

    return registro_lido


def atualizar_registro(caminho: str, index: int, dados: Registro) -> None:
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)


def deletar_registro(caminho: str, index: int) -> None:
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)
