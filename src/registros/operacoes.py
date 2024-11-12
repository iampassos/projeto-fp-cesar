from .. import ferramentas
from .registro import Registro

registro_caminho = "registros.csv"


def adicionar_registro(caminho: str, dados: Registro) -> Registro:
    """
    Adiciona um novo registro ao arquivo CSV.

    Argumentos:
        caminho (str): Caminho do diretório onde o arquivo CSV está localizado.
        dados (Registro): O registro a ser adicionado ao arquivo.

    Retorna:
        Registro: O registro adicionado ao arquivo.

    Exemplo de uso:
        novo_registro = adicionar_registro("/caminho/para", dados)
    """
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
    """
    Verifica se o índice fornecido é válido para o arquivo.

    Argumentos:
        index (int): O índice a ser verificado.
        arquivo (list): A lista de registros.

    Retorna:
        bool: True se o índice for válido, caso contrário False.

    Exemplo de uso:
        is_valid = index_valido(2, arquivo)
    """
    return index >= 1 and index < len(arquivo)


def ler_registro(caminho: str, index: int = None) -> Registro | list[Registro] | None:
    """
    Lê um registro do arquivo CSV ou todos os registros.

    Argumentos:
        caminho (str): Caminho do diretório onde o arquivo CSV está localizado.
        index (int, opcional): O índice do registro a ser lido.

    Retorna:
        Registro | list[Registro] | None: O registro lido ou uma lista de registros, ou None caso não encontrado.

    Exemplo de uso:
        registros = ler_registro("/caminho/para")
        registro = ler_registro("/caminho/para", 2)
    """
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index:
        return [Registro(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    registro_lido = Registro(*arquivo[index])

    return registro_lido


def atualizar_registro(caminho: str, index: int, dados: Registro) -> None:
    """
    Atualiza um registro no arquivo CSV com novos dados.

    Argumentos:
        caminho (str): Caminho do diretório onde o arquivo CSV está localizado.
        index (int): O índice do registro a ser atualizado.
        dados (Registro): O novo registro a ser escrito.

    Exemplo de uso:
        atualizar_registro("/caminho/para", 2, dados)
    """
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)


def deletar_registro(caminho: str, index: int) -> None:
    """
    Deleta um registro do arquivo CSV.

    Argumentos:
        caminho (str): Caminho do diretório onde o arquivo CSV está localizado.
        index (int): O índice do registro a ser deletado.

    Exemplo de uso:
        deletar_registro("/caminho/para", 2)
    """
    arquivo = ferramentas.ler_csv(caminho + registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(caminho + registro_caminho, arquivo)
