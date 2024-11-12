from .. import ferramentas
from . import registro as Registro

registro_caminho: str = "registros.csv"


def adicionar_registro(caminho: str, dados: Registro) -> list[str]:
    arquivo: list[list[str]] = ferramentas.ler_csv(caminho + registro_caminho)

    atributos: list[str] = [
        "tipo",
        "data",
        "distancia",
        "duracao",
        "localizacao",
        "clima",
    ]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_registro: list[str] = dados.__dict__.values()
    arquivo.append(novo_registro)

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)

    return novo_registro


def index_valido(index: int, arquivo: list[list[str]]) -> bool:
    return index >= 0 and index < len(arquivo)


def ler_registro(caminho: str, index: int = None):
    arquivo: list[list[str]] = ferramentas.ler_csv(caminho + registro_caminho)

    if not index:
        return [Registro(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    registro: Registro = Registro(*arquivo[index])

    return registro


def atualizar_registro(caminho: str, index: int, dados: Registro) -> None:
    arquivo: list[list[str]] = ferramentas.ler_csv(caminho + registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)


def deletar_registro(caminho: str, index: int) -> None:
    arquivo: list[list[str]] = ferramentas.ler_csv(caminho + registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)


