from .. import ferramentas
from .meta import Meta

metas_caminho = "metas.csv"


def adicionar_meta(caminho: str, dados: Meta) -> Meta:
    """
    Adiciona uma nova meta ao arquivo CSV.

    Argumentos:
        caminho (str): Caminho onde o arquivo CSV está localizado.
        dados (Meta): Dados da meta a ser adicionada.

    Retorna:
        Meta: A nova meta adicionada.

    Exemplo de uso:
        adicionar_meta("/path/to/", nova_meta)
    """
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    atributos = ["tipo", "distancia", "tempo"]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    nova_meta = list(dados.__dict__.values())
    arquivo.append(nova_meta)

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)

    return Meta(*nova_meta)


def index_valido(index: int, arquivo: list) -> bool:
    """
    Verifica se o índice informado é válido no arquivo.

    Argumentos:
        index (int): O índice a ser verificado.
        arquivo (list): A lista de metas do arquivo.

    Retorna:
        bool: Verdadeiro se o índice for válido, falso caso contrário.

    Exemplo de uso:
        index_valido(2, arquivo)
    """
    return index >= 0 and index < len(arquivo)


def ler_meta(caminho: str, index: int = None) -> Meta | list[Meta] | None:
    """
    Lê uma ou todas as metas do arquivo CSV.

    Argumentos:
        caminho (str): Caminho do arquivo CSV.
        index (int, opcional): Índice de uma meta específica. Se não fornecido, todas as metas são lidas.

    Retorna:
        Meta | list[Meta] | None: A meta específica ou uma lista de metas.

    Exemplo de uso:
        ler_meta("/path/to/", 2)
    """
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index:
        return [Meta(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    return Meta(*arquivo[index])


def atualizar_meta(caminho: str, index: int, dados: Meta) -> None:
    """
    Atualiza uma meta existente no arquivo CSV.

    Argumentos:
        caminho (str): Caminho onde o arquivo CSV está localizado.
        index (int): Índice da meta a ser atualizada.
        dados (Meta): Dados da meta a ser atualizada.

    Exemplo de uso:
        atualizar_meta("/path/to/", 3, meta_atualizada)
    """
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)


def deletar_meta(caminho: str, index: int) -> None:
    """
    Deleta uma meta do arquivo CSV.

    Argumentos:
        caminho (str): Caminho onde o arquivo CSV está localizado.
        index (int): Índice da meta a ser deletada.

    Exemplo de uso:
        deletar_meta("/path/to/", 2)
    """
    arquivo = ferramentas.ler_csv(caminho + metas_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(caminho + metas_caminho, arquivo)
