from .. import ferramentas
from .registro import Registro

registro_caminho: str = "./data/registros.csv"


def adicionar_registro(dados: Registro) -> list[str]:
    """
    Adiciona um novo registro de treino ou competição ao arquivo CSV.

    A função lê o conteúdo atual de um arquivo CSV, adiciona um novo registro de treino ou competição
    baseado nos dados fornecidos, e grava o arquivo atualizado. Se o arquivo estiver vazio, ele adiciona
    um cabeçalho com os atributos: "tipo", "data", "distancia", "duracao", "localizacao" e "clima".

    Args:
        dados (Registro): Objeto da classe `Registro` contendo os detalhes do treino ou competição a serem adicionados.

    Returns:
        list[str]: Lista de strings representando o novo registro, formatado como uma linha do CSV.

    Dependências:
        ferramentas.ler_csv: Função para ler o conteúdo do CSV.
        ferramentas.escrever_csv: Função para escrever dados no CSV.

    Exemplo de uso:
        registro = Registro("treino", "01/01/24", 5, 30, "Parque", "Ensolarado")
        novo_registro = adicionar_registro(registro)
        print(novo_registro)  # Exibirá o novo registro adicionado.
    """
    arquivo: list[list[str]] = ferramentas.ler_csv(registro_caminho)

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

    ferramentas.escrever_csv(registro_caminho, arquivo)

    return novo_registro


def index_valido(index: int, arquivo: list[list[str]]) -> bool:
    """
    Verifica se um índice é válido para acessar um registro em um arquivo CSV.

    A função verifica se o índice fornecido está dentro do intervalo válido para acessar os registros
    no arquivo, garantindo que o índice esteja dentro dos limites da lista.

    Args:
        index (int): Índice a ser verificado.
        arquivo (list[list[str]]): Lista de listas que representa o conteúdo do arquivo CSV.

    Returns:
        bool: `True` se o índice for válido (dentro dos limites do arquivo), `False` caso contrário.

    Exemplo de uso:
        valido = index_valido(3, arquivo)  # Retorna `True` se o índice 3 existir no arquivo.
    """
    return index >= 0 and index < len(arquivo)


def ler_registro(index: int = None) -> Registro | list[Registro] | None:
    """
    Lê um ou todos os registros de treino ou competição de um arquivo CSV.

    A função lê o conteúdo do arquivo CSV e retorna um registro específico ou uma lista de todos os registros.
    Se um índice for fornecido, ela retorna apenas o registro correspondente. Caso o índice não seja válido,
    retorna `None`. Se nenhum índice for passado, retorna uma lista com todos os registros.

    Args:
        index (int, opcional): Índice do registro a ser retornado. Se `None`, todos os registros serão retornados.

    Returns:
        Registro | list[Registro] | None:
            - `Registro`: Um único objeto `Registro` se o índice for válido.
            - `list[Registro]`: Lista de todos os registros se nenhum índice for fornecido.
            - `None`: Se o índice não for válido.

    Dependências:
        ferramentas.ler_csv: Função para ler o conteúdo do CSV.
        index_valido: Função para verificar se o índice fornecido é válido.

    Exemplo de uso:
        todos_registros = ler_registro()  # Retorna todos os registros.
        registro_especifico = ler_registro(2)  # Retorna o registro no índice 2, se válido.
    """
    arquivo: list[list[str]] = ferramentas.ler_csv(registro_caminho)

    if not index:
        return [Registro(*dados) for dados in arquivo]

    if not index_valido(index, arquivo):
        return None

    registro: Registro = Registro(*arquivo[index])

    return registro


def atualizar_registro(index: int, dados: Registro) -> None:
    """
    Atualiza um registro específico em um arquivo CSV com os novos dados fornecidos.

    A função lê o conteúdo do arquivo CSV, substitui o registro no índice especificado pelos dados
    fornecidos e grava o arquivo atualizado. Caso o índice fornecido seja inválido, a função não
    realiza nenhuma ação.

    Args:
        index (int): Índice do registro a ser atualizado.
        dados (Registro): Objeto `Registro` contendo os novos dados para atualizar o registro no índice fornecido.

    Returns:
        None: A função não retorna nada. Se o índice não for válido, a função termina sem modificar o arquivo.

    Dependências:
        ferramentas.ler_csv: Função para ler o conteúdo do CSV.
        ferramentas.escrever_csv: Função para gravar dados no CSV.
        index_valido: Função para verificar se o índice fornecido é válido.

    Exemplo de uso:
        novo_dados = Registro("treino", "02/02/24", 10, 45, "Academia", "Nublado")
        atualizar_registro(1, novo_dados)  # Atualiza o registro no índice 1 com os novos dados.
    """
    arquivo: list[list[str]] = ferramentas.ler_csv(registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(registro_caminho, arquivo)


def deletar_registro(index: int) -> None:
    """
    Deleta um registro específico de um arquivo CSV com base no índice fornecido.

    A função lê o conteúdo do arquivo CSV, remove o registro localizado no índice especificado e
    salva o arquivo atualizado. Caso o índice seja inválido, a função não realiza nenhuma ação.

    Args:
        index (int): Índice do registro a ser removido do arquivo CSV.

    Returns:
        None: A função não retorna nada. Se o índice não for válido, a função termina sem modificar o arquivo.

    Dependências:
        ferramentas.ler_csv: Função para ler o conteúdo do CSV.
        ferramentas.escrever_csv: Função para salvar dados no CSV.
        index_valido: Função para verificar se o índice fornecido é válido.

    Exemplo de uso:
        deletar_registro(2)  # Remove o registro no índice 2, se o índice for válido.
    """
    arquivo: list[list[str]] = ferramentas.ler_csv(registro_caminho)

    if not index_valido(index, arquivo):
        return None

    arquivo.pop(index)

    ferramentas.escrever_csv(registro_caminho, arquivo)


adicionar_registro(Registro("treino", "12/11/2022", 56, 34, "Recife", "clima"))
