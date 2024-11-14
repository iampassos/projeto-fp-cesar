from ..autenticacao import operacoes as usuario_operacoes
from ..autenticacao.usuario import Usuario
from ..metas.meta import Meta
from ..metas.operacoes import adicionar_meta, ler_meta

from . import ferramentas as f

def nova_meta_desafio_input(usuario, erro = None):
    f.clear()

    if erro:
        f.texto_centralizado(erro, 2)

    f.texto_centralizado('Escolha uma opção para continuar ou "q" para voltar', -6)

    f.textos_centralizados(
        "1 - Meta de distância",
        "2 - Meta de tempo",
        acima=1
    )

    opcao = f.input_centralizado("Opção Desejada: ")

    if opcao == "1":
        distancia = f.input_centralizado("Digite a distância desejada: ")

        if not f.is_float(distancia) or float(distancia) <= 0:
            return nova_meta_desafio_input(usuario, "A distância deve ser um número maior que 0")
        meta = Meta("Distância", distancia, 0)
    elif opcao == "2":
        tempo = f.input_centralizado("Digite o tempo desejado: ")
        if not f.is_float(tempo) or float(tempo) <= 0:
            return nova_meta_desafio_input(usuario, "O tempo deve ser um número maior que 0")
        meta = Meta("Tempo", 0, tempo)
    else:
        return nova_meta_desafio_input(usuario, "Meta não adicionada")

    adicionar_meta(f"data/{usuario.email}/", meta)

    return "Meta adicionada"

def acompanhar_metas(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    metas: list[Meta] = ler_meta(
        f"data/{usuario.email}/")

    if len(metas) <= 1:
        return "Não há metas para serem mostrados!"

    printados = []

    for i, j in enumerate(metas):
        if i == 0:
            values = list(j.__dict__.values())
            values.insert(0, "Índice")
            printados.append(
                f"| {" | ".join([f"{k.capitalize():^12}" for k in values])} |")
            printados.append("-" * len(printados[0]))
        else:
            values = j.__str__().split(", ")
            values.insert(0, str(i))
            printados.append(f"| {" | ".join([f"{v:^12}" for v in values])} |")

    printados.append("-" * len(printados[0]))

    f.textos_centralizados(*printados, acima=-len(printados) // 2)

    input(f.centralizar_meio_inferior("Pressione Enter para voltar"))

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


def tela_metas(usuario: Usuario, mensagem=None):
    opcao = inicial(usuario, mensagem)

    while opcao != "q":
        if opcao == "1":
            mensagem = nova_meta_desafio_input(usuario)
        elif opcao == "2":
            mensagem = acompanhar_metas(usuario)
        elif opcao == "3":
            pass

        opcao = inicial(usuario, mensagem)
