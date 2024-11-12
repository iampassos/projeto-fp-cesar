import os


def ler_csv(caminho: str, criar: bool = True) -> list:
    if not os.path.exists(caminho) and criar:
        escrever_csv(caminho, [])

    with open(caminho, "r", encoding="utf8") as arquivo:
        dados = []

        for linha in arquivo.readlines():
            formato = linha.strip().split(",")
            dados.append(formato)

    return dados


def escrever_csv(caminho: str, dados: list) -> None:
    with open(caminho, "w", encoding="utf8") as arquivo:
        for formato in dados:
            linha = ",".join(str(valor) for valor in formato)
            arquivo.write(f"{linha}\n")
