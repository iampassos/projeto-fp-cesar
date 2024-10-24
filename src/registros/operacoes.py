from .. import ferramentas
from . import registro as Registro


registro_caminho = "./data/registros.csv"


# Adiciona um registro ao banco de dados
# Retorna os dados em uma lista

def adicionar_registro(dados: Registro.Registro):
    arquivo = ferramentas.ler_csv(registro_caminho)

    atributos = ["tipo", "data", "distancia",
                 "duracao", "localizacao", "clima"]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_registro = [str(getattr(dados, i)) for i in atributos]
    arquivo.append(novo_registro)

    ferramentas.escrever_csv(registro_caminho, arquivo)

    return novo_registro


# Ler um registro do banco de dados baseado no índice (começa no 1)
# Retorna os dados na classe Registro ou None caso não exista

def ler_registro(index=None):
    arquivo = ferramentas.ler_csv(registro_caminho)

    if not index:
        return [Registro.Registro(*dados) for dados in arquivo]

    if index >= len(arquivo) or index < 0:
        return None

    dados = arquivo[index]
    registro = Registro.Registro(*dados)

    return registro


# Atualizar um registro do banco de dados baseado no índice (começa no 1)
# Retorna os novos dados na classe Registro ou None caso não exista

def atualizar_registro(index, dados: Registro.Registro):
    registro = ler_registro(index)

    if not registro:
        return None

    arquivo = ferramentas.ler_csv(registro_caminho)
    arquivo[index] = [*dados.__dict__.values()]

    ferramentas.escrever_csv(registro_caminho, arquivo)

    return dados


# Deletar um registro do banco de dados baseado no índice (começa no 1)
# Retorna None caso não exista

def deletar_registro(index):
    registro = ler_registro(index)

    if not registro:
        return None

    arquivo = ferramentas.ler_csv(registro_caminho)
    arquivo.pop(index)

    ferramentas.escrever_csv(registro_caminho, arquivo)

