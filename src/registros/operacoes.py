from .. import ferramentas
from . import registro as Registro

# Caminho do arquivo CSV que armazena os registros
registro_caminho = "./data/registros.csv"


def adicionar_registro(dados: Registro.Registro):
    """
    Adiciona um novo registro ao banco de dados CSV.

    Args:
        dados (Registro.Registro): Instância da classe Registro contendo os
        dados do registro a ser adicionado.

    Returns:
        list: Lista contendo os valores do novo registro.
    """
    arquivo = ferramentas.ler_csv(registro_caminho)
    atributos = ["tipo", "data", "distancia",
                 "duracao", "localizacao", "clima"]

    # Se o arquivo estiver vazio, adiciona o cabeçalho
    if len(arquivo) == 0:
        arquivo.append(atributos)

    # Extrai os valores dos atributos do objeto dados e adiciona ao arquivo
    novo_registro = [str(getattr(dados, i)) for i in atributos]
    arquivo.append(novo_registro)

    ferramentas.escrever_csv(registro_caminho, arquivo)
    return novo_registro


def ler_registro(index=None):
    """
    Lê um ou mais registros do banco de dados CSV.

    Args:
        index (int, optional): Índice do registro a ser lido (começa em 1).
                               Se None, retorna todos os registros.

    Returns:
        list | Registro.Registro | None:
            - Lista de todos os registros como objetos Registro se
            `index` for None.
            - Um único registro como objeto Registro se o `index` for válido.
            - None se o índice fornecido for inválido.
    """
    arquivo = ferramentas.ler_csv(registro_caminho)

    if index is None:
        return [Registro.Registro(*dados) for dados in arquivo]

    if index >= len(arquivo) or index < 0:
        return None

    registro = Registro.Registro(*arquivo[index])
    return registro


def atualizar_registro(index, dados: Registro.Registro):
    """
    Atualiza um registro no banco de dados CSV com novos dados.

    Args:
        index (int): Índice do registro a ser atualizado (começa em 1).
        dados (Registro.Registro): Instância da classe Registro contendo
        os novos dados.

    Returns:
        Registro.Registro | None:
            - Objeto Registro atualizado se o índice for válido.
            - None se o índice fornecido for inválido.
    """
    registro = ler_registro(index)

    if not registro:
        return None

    arquivo = ferramentas.ler_csv(registro_caminho)
    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(registro_caminho, arquivo)
    return dados


def deletar_registro(index):
    """
    Remove um registro do banco de dados CSV.

    Args:
        index (int): Índice do registro a ser removido (começa em 1).

    Returns:
        None: Retorna None se o índice fornecido for inválido ou após
        remover o registro.
    """
    registro = ler_registro(index)

    if not registro:
        return None

    arquivo = ferramentas.ler_csv(registro_caminho)
    arquivo.pop(index)

    ferramentas.escrever_csv(registro_caminho, arquivo)
