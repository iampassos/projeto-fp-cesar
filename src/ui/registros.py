from ..data import Data
from . import ferramentas as f
from ..autenticacao.usuario import Usuario

from ..registros import operacoes
from ..registros import funcionalidades

from .. import registros

Registro = registros.registro.Registro


def inicial(usuario: Usuario, mensagem=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Escolha uma opção para continuar ou "q" para voltar', -8)

    f.textos_centralizados(
        "1 - Adicionar Treinos ou Competições",
        "2 - Visualizar Treinos ou Competições",
        "3 - Atualizar Treinos ou Competições",
        "4 - Sugerir Treino ou Competição",
        "5 - Deletar Treinos ou Competições",
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

        if not (0 < colocada.dia < 32):
            raise ValueError()

        if not (0 < colocada.mes < 13):
            raise ValueError()

        if colocada.ano < 0:
            raise ValueError()

        colocada_v = colocada.dia + colocada.mes * 31 + colocada.ano * 372
        atual_v = atual.dia + atual.mes * 31 + atual.ano * 372

        if colocada_v > atual_v:
            raise ValueError()
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

    return "Treino/Competição adicionado!"


def modo_visualizar_registros(usuario: Usuario, mensagem=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Escolha uma opção para continuar ou "q" para voltar', -6)

    f.textos_centralizados(
        "1 - Visualizar Todos os Treinos e Competições",
        "2 - Filtrar por Distância",
        "3 - Filtrar por Duração",
        acima=1
    )

    if mensagem:
        f.texto_centralizado(mensagem, 2)

    return f.input_centralizado("Opção Desejada: ")


def filtro_distancia(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    dist = f.input_centralizado("Distância para Filtrar (km): ")

    if dist == "q":
        return None

    if not dist or not f.is_float(dist):
        return filtro_distancia(usuario, "Distância inválida")

    return dist


def filtro_duracao(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    dur = f.input_centralizado("Duração para Filtrar (min): ")

    if dur == "q":
        return None

    if not dur or not f.is_float(dur):
        return filtro_distancia(usuario, "Duração inválida")

    return dur


def visualizar_registros(usuario: Usuario, erro=None, filtro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    registros: list[Registro] = operacoes.ler_registro(
        f"data/{usuario.email}/")

    if len(registros) <= 1:
        return "Não há registros para serem mostrados!"

    coluna = registros[0]

    if filtro == "distancia":
        resultado = filtro_distancia(usuario)

        if resultado is None:
            return None

        registros = funcionalidades.filtrar(
            registros[1:], "distancia", float(resultado))

        registros.insert(0, coluna)

    if filtro == "duracao":
        resultado = filtro_duracao(usuario)

        if resultado is None:
            return None

        registros = funcionalidades.filtrar(
            registros[1:], "duracao", float(resultado))

        registros.insert(0, coluna)

    if len(registros) <= 1:
        return "Não há registros para serem mostrados!"

    printados = []

    for i, j in enumerate(registros):
        if i == 0:
            values = list(j.__dict__.values())
            values.insert(0, "Índice")
            printados.append(
                f"| {" | ".join([f"{k.capitalize():^12}" for k in values])} |")
            printados.append("-" * len(printados[0]))
        else:
            values = j.__str__().split(", ")
            values.insert(0, str(i))
            printados.append(
                f"| {" | ".join([f"{k:^12}" for k in values])} |")

    printados.append("-" * len(printados[0]))

    f.textos_centralizados(*printados, acima=-len(printados) // 2)

    input(f.centralizar_meio_inferior("Pressione Enter para voltar"))


def atualizar_registro(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" no índice para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    index = f.input_centralizado("Índice do Registro: ")

    if index == "q":
        return None

    registros = operacoes.ler_registro(f"data/{usuario.email}/")

    try:
        index = int(index)

        if not operacoes.index_valido(index, registros):
            raise ValueError()
    except ValueError:
        return atualizar_registro(usuario, "Índice inválido!")

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
        respostas.append(f.input_centralizado(j, i - 3) or None)

        if i == 0 and respostas[0] == "q":
            return None

    tipo, data, distancia, duracao, localizacao, clima = respostas

    if tipo:
        if tipo.lower() not in ["treino", "competicao"]:
            return atualizar_registro(usuario, "Tipo de registro inválido!")

    try:
        if data:
            if len(data.split("/")) != 3 or len(data.split("/")[2]) != 4:
                raise ValueError()

            colocada = Data(data.strip())
            atual = Data.data_atual()

            if atual.ano < colocada.ano % 100 or atual.mes < colocada.mes % 100 or atual.dia < colocada.dia % 100:
                raise ValueError
    except ValueError:
        return atualizar_registro(usuario, "Data inválida!")

    try:
        if distancia:
            distancia = float(distancia)

            if distancia <= 0:
                raise ValueError()
    except ValueError:
        return atualizar_registro(usuario, "Distância inválida!")

    try:
        if duracao:
            duracao = float(duracao)

            if duracao <= 0:
                raise ValueError()
    except ValueError:
        return atualizar_registro(usuario, "Duracao inválida!")

    reg = registros[index]

    operacoes.atualizar_registro(
        f"data/{usuario.email}/", index, Registro(tipo or reg.tipo, data or reg.data, distancia or reg.distancia, duracao or reg.duracao, localizacao or reg.localizacao, clima or reg.clima))

    return "Treino/Competição atualizado!"


def deletar_registro(usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    index = f.input_centralizado("Índice do Registro: ")

    if index == "q":
        return None

    registros = operacoes.ler_registro(f"data/{usuario.email}/")

    try:
        index = int(index)

        if not operacoes.index_valido(index, registros) or float(index) == 0:
            raise ValueError()
    except ValueError:
        return deletar_registro(usuario, "Índice inválido!")

    operacoes.deletar_registro(f"data/{usuario.email}/", index)

    return "Treino/Competição Deletado!"


def sugerir_registro(usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    incremento = f.input_centralizado(
        "Incremento de Dificuldade em Percentual (float): ")

    if incremento == "q":
        return None

    if not f.is_float(incremento) or float(incremento) < 0:
        return sugerir_registro(usuario, "O incremento deve ser um número em percentual!")

    historico = operacoes.ler_registro(f"data/{usuario.email}/")

    registro = funcionalidades.sugerir_treino(
        historico[1:], float(incremento) / 100)

    printados = []

    values = list(historico[0].__dict__.values())
    values.insert(0, "Índice")
    printados.append(
        f"| {" | ".join([f"{k.capitalize():^12}" for k in values])} |")
    printados.append("-" * len(printados[0]))

    values = registro.__str__().split(", ")
    values.insert(0, str(1))
    printados.append(
        f"| {" | ".join([f"{k:^12}" for k in values])} |")

    printados.append("-" * len(printados[0]))

    f.textos_centralizados(*printados, acima=-len(printados) // 2)

    input(f.centralizar_meio_inferior("Pressione Enter para voltar"))

    return "Treino sugerido!"


def tela_registros(usuario: Usuario, mensagem=None):
    opcao = inicial(usuario, mensagem)

    while opcao != "q":
        if opcao == "1":
            mensagem = adicionar_registro(usuario)
        elif opcao == "2":
            opcao_modo = modo_visualizar_registros(usuario)
            mensagem_nova = None

            while opcao_modo != "q":
                if opcao_modo == "1":
                    mensagem_nova = visualizar_registros(usuario)
                elif opcao_modo == "2":
                    mensagem_nova = visualizar_registros(
                        usuario, filtro="distancia")
                elif opcao_modo == "3":
                    mensagem_nova = visualizar_registros(
                        usuario, filtro="duracao")

                opcao_modo = modo_visualizar_registros(usuario, mensagem_nova)
        elif opcao == "3":
            mensagem = atualizar_registro(usuario)
        elif opcao == "4":
            mensagem = sugerir_registro(usuario)
        elif opcao == "5":
            mensagem = deletar_registro(usuario)

        opcao = inicial(usuario, mensagem)
