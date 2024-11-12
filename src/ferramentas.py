import os


def ler_csv(caminho: str, criar: bool = True) -> list:
    """
    Lê um arquivo CSV e retorna seu conteúdo como uma lista de listas de strings.

    Se o arquivo não existir, ele será criado, se o parâmetro 'criar' for True.

    Argumentos:
        caminho (str): Caminho do arquivo CSV a ser lido.
        criar (bool, opcional): Indica se o arquivo deve ser criado caso não exista (padrão é True).

    Retorna:
        list: Uma lista de listas contendo os dados lidos do arquivo CSV.

    Exemplo de uso:
        dados = ler_csv("/caminho/para/arquivo.csv")
    """
    if not os.path.exists(caminho) and criar:
        escrever_csv(caminho, [])

    with open(caminho, "r", encoding="utf8") as arquivo:
        dados = []

        for linha in arquivo.readlines():
            formato = linha.strip().split(",")
            dados.append(formato)

    return dados


def escrever_csv(caminho: str, dados: list) -> None:
    """
    Escreve uma lista de dados em um arquivo CSV.

    Argumentos:
        caminho (str): Caminho do arquivo CSV onde os dados serão escritos.
        dados (list): Lista de listas contendo os dados a serem gravados no arquivo CSV.

    Exemplo de uso:
        escrever_csv("/caminho/para/arquivo.csv", dados)
    """
    with open(caminho, "w", encoding="utf8") as arquivo:
        for formato in dados:
            linha = ",".join(str(valor) for valor in formato)
            arquivo.write(f"{linha}\n")
