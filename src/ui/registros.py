from ..data import Data
from . import ferramentas as f
from ..autenticacao.usuario import Usuario

# from ..registros.registro import Registro
from ..registros import operacoes

from .. import registros

Registro = registros.registro.Registro


def inicial(usuario: Usuario, mensagem=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Escolha uma opção para continuar ou "q" para voltar', -7)

    f.textos_centralizados(
        "1 - Adicionar Treinos ou Competições",
        "2 - Visualizar Treinos ou Competições",
        "3 - Atualizar Treinos ou Competições",
        "4 - Deletar Treinos ou Competições",
        acima=1
    )

    if mensagem:
        f.texto_centralizado(mensagem, 2)

    return f.input_centralizado("Opção Desejada: ")


def adicionar_registro(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" no tipo para voltar', -5)

    perguntas = ["Tipo (Treino/Competicao): ", "Data (DD/MM/YYYY): ",
                 "Distância (km): ", "Duração (min): ", "Localização: ", "Clima: "]

    for i, j in enumerate(perguntas):
        f.texto_centralizado(j, i - 3)

    if erro:
        f.texto_centralizado(erro, 4)

    respostas = []

    for i, j in enumerate(perguntas):
        respostas.append(f.input_centralizado(j, i - 3))

        if not respostas[i]:
            return adicionar_registro(usuario, "Campo inválido!")

        if i == 0 and respostas[0] == "q":
            return None

    tipo, data, distancia, duracao, localizacao, clima = respostas

    if tipo.lower() not in ["treino", "competicao"]:
        return adicionar_registro(usuario, "Tipo de registro inválido!")

    try:
        if len(data.split("/")) != 3 or len(data.split("/")[2]) != 4:
            raise ValueError()

        colocada = Data(data.strip())
        atual = Data.data_atual()

        if atual.ano < colocada.ano % 100 or atual.mes < colocada.mes % 100 or atual.dia < colocada.dia % 100:
            raise ValueError
    except ValueError:
        return adicionar_registro(usuario, "Data inválida!")

    try:
        distancia = float(distancia)

        if distancia <= 0:
            raise ValueError()
    except ValueError:
        return adicionar_registro(usuario, "Distância inválida!")

    try:
        duracao = float(duracao)

        if duracao <= 0:
            raise ValueError()
    except ValueError:
        return adicionar_registro(usuario, "Duracao inválida!")

    operacoes.adicionar_registro(
        f"data/{usuario.email}/", Registro(tipo, data, distancia, duracao, localizacao, clima))

    return "Registro adicionado!"


def visualizar_registros(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    registros: list[Registro] = operacoes.ler_registro(
        f"data/{usuario.email}/")

    f.texto_centralizado(
        'Digite qualquer tecla para voltar', -(len(registros) // 2) * 2 - 2)

    if len(registros) <= 1:
        return "Não há registros para serem mostrados!"

    printados = []

    for i, j in enumerate(registros):
        if i == 0:
            values = list(j.__dict__.values())
            values.insert(0, "Índice")
            printados.append(
                f"| {" | ".join([k.capitalize() for k in values])} |")
        else:
            values = j.__str__().split(", ")
            values.insert(0, str(i))
            printados.append(f"| {" | ".join(values)} |")

    f.textos_centralizados(*printados)

    f.input_centralizado("Sair: ", (len(registros) // 2) - 1)


def deletar_registro(usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" no índice para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    index = f.input_centralizado("Índice do Registro: ")

    if index == "q":
        return "q"

    try:
        index = int(index)

        if not index or index <= 0:
            raise ValueError()
    except ValueError:
        return deletar_registro(usuario, "Índice inválido!")

    operacoes.deletar_registro(f"data/{usuario.email}/", index)

    return "Registro Deletado!"


def tela_registros(usuario: Usuario, mensagem=None):
    opcao = inicial(usuario, mensagem)

    while opcao != "q":
        if opcao == "1":
            mensagem = adicionar_registro(usuario)
        elif opcao == "2":
            mensagem = visualizar_registros(usuario)
        elif opcao == "4":
            mensagem = deletar_registro(usuario)

        opcao = inicial(usuario, mensagem)