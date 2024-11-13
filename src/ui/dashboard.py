from ..autenticacao.usuario import Usuario

from . import ferramentas as f


def inicial(usuario: Usuario):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Escolha uma opção para continuar ou "q" para deslogar', -6)

    f.textos_centralizados(
        "1 - Treinos e Competições",
        "2 - Metas e Desafios",
        "3 - Gerenciar Conta",
        acima=1
    )

    return f.input_centralizado("Opção Desejada: ")


def tela_dashboard(usuario: Usuario):
    return inicial(usuario)

