from ..autenticacao import operacoes as usuario_operacoes
from ..autenticacao.usuario import Usuario

from . import ferramentas as f


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
            pass
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass

        opcao = inicial(usuario, mensagem)
