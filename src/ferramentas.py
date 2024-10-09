# Ler de arquivo .csv
# Essa função vai tratar os dados do arquivo .csv e vai retornar uma lista
# com todos os dados
# Ex: [["nome", "idade"], ["João", 17], ["Mircio", 18]]


def lerCSV(caminho):
    with open(caminho, "r") as arquivo:
        dados = []

        for linha in arquivo.readlines():
            formato = linha.strip().split(",")
            dados.append(formato)

    return dados


# Escrever para arquivo .csv
# Essa função vai escrever para o arquivo .csv no formato que ele precisa.
# Aqui você pode reescrever o banco de dados inteiro, então cuidado
# Ex: [["nome", "idade"], ["João", 17], ["Mircio", 18]]


def escreverCSV(caminho, dados):
    with open(caminho, "w") as arquivo:
        for formato in dados:
            linha = ",".join(str(valor) for valor in formato)
            arquivo.write(f"{linha}\n")
