import os

"""
Ler de arquivo .csv
Essa função vai tratar os dados do arquivo .csv e vai retornar uma lista
com todos os dados. Ela cria um novo arquivo caso ele não exista
Ex: [["nome", "idade"], ["João", 17], ["Mircio", 18]]
"""


def ler_csv(caminho):
    if not os.path.exists(caminho):
        escrever_csv(caminho, [])

    with open(caminho, "r", encoding="utf8") as arquivo:
        dados = []

        for linha in arquivo.readlines():
            formato = linha.strip().split(",")
            dados.append(formato)

    return dados


"""
Escrever para arquivo .csv
Essa função vai escrever para o arquivo .csv no formato que ele precisa.
Aqui você pode reescrever o banco de dados inteiro, então cuidado
Ex: [["nome", "idade"], ["João", 17], ["Mircio", 18]]
"""


def escrever_csv(caminho, dados):
    with open(caminho, "w", encoding="utf8") as arquivo:
        for formato in dados:
            linha = ",".join(str(valor) for valor in formato)
            arquivo.write(f"{linha}\n")
