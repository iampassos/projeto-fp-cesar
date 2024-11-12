import os


def ler_csv(caminho, criar=True):
    """
    Lê dados de um arquivo CSV.

    Esta função trata os dados de um arquivo CSV e retorna uma lista
    contendo todos os dados. Caso o arquivo não exista, ele é criado
    automaticamente como um arquivo vazio.

    Args:
        caminho (str): Caminho do arquivo CSV a ser lido.

    Returns:
        list: Lista de listas contendo os dados do CSV.
              Exemplo: [["nome", "idade"], ["João", 17], ["Mircio", 18]]
    """
    if not os.path.exists(caminho) and criar:
        escrever_csv(caminho, [])

    with open(caminho, "r", encoding="utf8") as arquivo:
        dados = []

        for linha in arquivo.readlines():
            formato = linha.strip().split(",")
            dados.append(formato)

    return dados[1:]


def escrever_csv(caminho, dados):
    """
    Escreve dados em um arquivo CSV.

    Esta função escreve a lista de dados fornecida para o arquivo CSV.
    É importante lembrar que esta função reescreve todo o conteúdo do arquivo,
    então use-a com cuidado para evitar a perda de dados.

    Args:
        caminho (str): Caminho do arquivo CSV onde os dados serão escritos.
        dados (list): Lista de listas contendo os dados a serem gravados no CSV
                    Exemplo: [["nome", "idade"], ["João", 17], ["Mircio", 18]]
    """
    with open(caminho, "w", encoding="utf8") as arquivo:
        for formato in dados:
            linha = ",".join(str(valor) for valor in formato)
            arquivo.write(f"{linha}\n")
