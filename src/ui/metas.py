from . import ferramentas as f
from ..autenticacao.usuario import Usuario
from ..registros import operacoes as registros

from .. import metas
from ..metas import operacoes
from ..metas import funcionalidades

Meta = metas.meta.Meta


def inicial(usuario: Usuario, mensagem=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Escolha uma opção para continuar ou "q" para voltar', -6)

    f.textos_centralizados(
        "1 - Nova Meta ou Desafio",
        "2 - Acompanhar Metas e Desafios",
        "3 - Deletar Meta ou Desafio",
        acima=1
    )

    if mensagem:
        f.texto_centralizado(mensagem, 2)

    return f.input_centralizado("Opção Desejada: ")


def escolher_tipo_meta(usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Escolha uma opção para continuar ou "q" para voltar', -5)

    f.textos_centralizados(
        "1 - Meta ou Desafio de Distância",
        "2 - Meta ou Desafio de Tempo",
        acima=1
    )

    if erro:
        f.texto_centralizado(erro, 2)

    return f.input_centralizado("Opção Desejada: ")


def adicionar_meta_distancia(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    distancia = f.input_centralizado("Distância (km): ")

    if distancia == "q":
        return None

    if not distancia or not f.is_float(distancia) or float(distancia) <= 0:
        return adicionar_meta_distancia(usuario, "Distância inválida!")

    operacoes.adicionar_meta(
        f"data/{usuario.email}/", Meta("distancia", distancia))

    return "Meta/Desafio Adicionado!"


def adicionar_meta_tempo(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" na distância para voltar', -3)

    perguntas = ["Distância (km): ", "Tempo (min): ",]

    for i, j in enumerate(perguntas):
        f.texto_centralizado(j, i - 1)

    if erro:
        f.texto_centralizado(erro, 2)

    metas: list[Meta] = operacoes.ler_meta(
        f"data/{usuario.email}/")

    for i, j in enumerate(metas):
        if i != 0 and j.tempo != "-1":
            return "Já existe uma Meta/Desafio de tempo ativo!"

    respostas = []

    for i, j in enumerate(perguntas):
        respostas.append(f.input_centralizado(j, i - 1))

        if not respostas[i]:
            return adicionar_meta_tempo(usuario, "Campo inválido!")

        if i == 0 and respostas[0] == "q":
            return None

    distancia, tempo = respostas

    if not distancia or not f.is_float(distancia) or float(distancia) <= 0:
        return adicionar_meta_tempo(usuario, "Distância inválida!")

    if not tempo or not f.is_float(tempo) or float(tempo) <= 0:
        return adicionar_meta_tempo(usuario, "Tempo inválido!")

    operacoes.adicionar_meta(
        f"data/{usuario.email}/", Meta("tempo", distancia, tempo))

    return "Meta/Desafio Adicionado!"


def acompanhar_metas(usuario: Usuario, erro=None, tipo="distancia"):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    metas: list[Meta] = operacoes.ler_meta(
        f"data/{usuario.email}/")

    if len(metas) <= 1:
        return "Não há metas ou desafios para serem mostrados!"

    printados = []

    regs = registros.ler_registro(f"data/{usuario.email}/")

    if tipo == "distancia":
        meta_distancia = 0

        for i, j in enumerate(metas):
            if i != 0 and j.tempo == "-1":
                meta_distancia += 1

        if meta_distancia == 0:
            return "Não há uma meta ou desafio de distância ativo!"

        for i, j in enumerate(metas):
            if i == 0:
                values = list(j.__dict__.values())
                values.insert(0, "Índice")
                values.__delitem__(3)
                values.append("Progresso")
                printados.append(
                    f"| {" | ".join([f"{k.capitalize():^12}" for k in values])} |")
                printados.append("-" * len(printados[0]))
            else:
                if j.tempo == "-1":
                    values = j.__str__().split(", ")
                    values.insert(0, str(i))
                    values.__delitem__(3)
                    total = funcionalidades.acompanhar_meta_distancia(
                        regs[1:], j)
                    if total[0] == 0:
                        return "Não há treinos ou competições para este mês!"
                    values.append(f"{total[1] * 100:.2f}%")
                    printados.append(
                        f"| {" | ".join([f"{k:^12}" for k in values])} |")

    elif tipo == "tempo":
        if len(regs) == 0:
            return "Não há treinos ou competições para se acompanhar!"

        meta_tempo = None

        for i, j in enumerate(metas):
            if i != 0 and j.tempo != "-1":
                meta_tempo = j

        if not meta_tempo:
            return "Não há uma meta ou desafio de tempo ativo!"

        for i, j in enumerate(regs):
            if i == 0:
                values = list(j.__dict__.values())
                values.insert(0, "Índice")
                values.append("Meta")
                printados.append(
                    f"| {" | ".join([f"{k.capitalize():^12}" for k in values])} |")
                printados.append("-" * len(printados[0]))
            elif meta_tempo:
                values = j.__str__().split(", ")
                values.insert(0, str(i))
                total = funcionalidades.acompanhar_meta_tempo(
                    regs[1:], meta_tempo)
                if len(total) == 0:
                    return "Não há treinos ou competições para este mês!"
                for v in total:
                    values.append("Bateu" if v[0] ==
                                  j and v[1] else "Não Bateu")
                printados.append(
                    f"| {" | ".join([f"{k:^12}" for k in values])} |")

                values = list(j.__dict__.values())

        print("".center(f.columns))

        topo = []
        for i, j in enumerate(metas):
            if i == 0:
                values = list(j.__dict__.values())
                values.insert(0, "Índice")
                topo.append(
                    f"| {" | ".join([f"{k.capitalize():^12}" for k in values])} |")
                topo.append("-" * len(topo[0]))
            elif meta_tempo == j:
                values = list(meta_tempo.__dict__.values())
                values.insert(0, metas.index(meta_tempo))
                topo.append(f"| {" | ".join([f"{k:^12}" for k in values])} |")

        topo.append("-" * len(topo[0]))

        for i in topo:
            print(i.center(f.columns))

    printados.append("-" * len(printados[0]))

    f.textos_centralizados(*printados, acima=-len(printados) // 2)

    input(f.centralizar_meio_inferior("Pressione Enter para voltar"))


def deletar_meta(usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" no índice para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    index = f.input_centralizado("Índice da Meta ou Desafio: ")

    if index == "q":
        return None

    metas = operacoes.ler_meta(f"data/{usuario.email}/")

    if not index or not f.is_int(index) or not operacoes.index_valido(int(index), metas):
        return deletar_meta(usuario, "Índice inválido!")

    operacoes.deletar_meta(f"data/{usuario.email}/", int(index))

    return "Meta/Desafio Deletado!"


def tela_metas(usuario: Usuario, mensagem=None):
    opcao = inicial(usuario, mensagem)

    while opcao != "q":
        if opcao == "1" or opcao == "2":
            opcao_tipo = escolher_tipo_meta(usuario)
            mensagem_nova = None

            while opcao_tipo != "q":
                if opcao == "1":
                    if opcao_tipo == "1":
                        mensagem_nova = adicionar_meta_distancia(usuario)
                    elif opcao_tipo == "2":
                        mensagem_nova = adicionar_meta_tempo(usuario)
                elif opcao == "2":
                    if opcao_tipo == "1":
                        mensagem_nova = acompanhar_metas(
                            usuario, tipo="distancia")
                    elif opcao_tipo == "2":
                        mensagem_nova = acompanhar_metas(usuario, tipo="tempo")

                opcao_tipo = escolher_tipo_meta(usuario, mensagem_nova)
        elif opcao == "3":
            mensagem = deletar_meta(usuario)

        opcao = inicial(usuario, mensagem)
