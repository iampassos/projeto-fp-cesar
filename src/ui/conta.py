from ..autenticacao.usuario import Usuario
from ..autenticacao import operacoes

from . import ferramentas as f


def inicial(usuario: Usuario, mensagem=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Escolha uma opção para continuar ou "q" para voltar', -6)
    f.texto_centralizado("1 - Atualizar Senha", -4)
    f.texto_centralizado("2 - Atualizar Nome", -3)
    f.texto_centralizado("3 - Deletar Conta", -2)

    if mensagem:
        f.texto_centralizado(mensagem, 2)
        return

    return f.input_centralizado("Opção Desejada: ")


def atualizar_senha(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    senha = f.input_centralizado("Nova Senha: ")

    if senha == "q":
        return None

    if not senha:
        return atualizar_senha(usuario, "Senha inválida!")

    novo = operacoes.atualizar_usuario(usuario.email, Usuario(
        usuario.nome, usuario.email, senha))

    return tela_conta(novo, "Senha alterada!")


def atualizar_nome(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    nome = f.input_centralizado("Novo Nome: ")

    if nome == "q":
        return None

    if not nome:
        return atualizar_nome(usuario, "Nome inválido!")

    novo = operacoes.atualizar_usuario(usuario.email, Usuario(
        nome, usuario.email, usuario.senha))

    return tela_conta(novo, "Nome alterado!")


def deletar_conta(usuario: Usuario, erro=None):
    f.clear()

    print(f"Você está logado como {usuario.nome} ({
          usuario.email})!".center(f.columns))

    f.texto_centralizado(
        'Digite "q" para voltar', -2)

    if erro:
        f.texto_centralizado(erro, 2)

    nome = f.input_centralizado("Seu Nome: ")

    if nome == "q":
        return None

    if not nome:
        return deletar_conta(usuario, "Nome inválido!")

    if nome != usuario.nome:
        return deletar_conta(usuario, "Nome não coincide com o da sua conta!")

    operacoes.deletar_usuario(usuario.email)


def tela_conta(usuario: Usuario, mensagem=None):
    opcao = inicial(usuario, mensagem)

    if opcao == "q":
        return "q"
    elif opcao == "1":
        atualizar_senha(usuario)
    elif opcao == "2":
        atualizar_nome(usuario)
    elif opcao == "3":
        resultado = deletar_conta(usuario)
        if resultado:
            return None

    return operacoes.ler_usuario(usuario.email)

