from ..autenticacao import operacoes as usuario_operacoes
from ..autenticacao.usuario import Usuario

from . import ferramentas as f


def inicial():
    f.clear()

    f.texto_centralizado(
        "Bem-vindo ao Corridinha, o aplicativo de gerenciamento de treinos e competições de corrida.", -2)
    f.texto_centralizado(
        "Você já tem uma conta cadastrada? Se sim, pressione 1. Caso contrário, pressione 2.")

    return f.input_centralizado("Opção Desejada: ", 2)


def login(erro=None):
    f.clear()
    print("Login Corridinha".center(f.columns))

    f.texto_centralizado('Digite "q" no email para voltar', -2)
    f.texto_centralizado("Senha: ", 1)

    if erro:
        f.texto_centralizado(erro, 3)

    email = f.input_centralizado("Email: ")

    if not email:
        return login("Email invalido!")

    senha = f.input_centralizado("Senha: ", 1)

    if not senha:
        return login("Senha invalida")

    usuario = usuario_operacoes.ler_usuario(email)

    if usuario:
        if usuario.senha == senha:
            return usuario
        else:
            return login("Senha incorreta!")
    else:
        return login("Email não cadastrado!")


def cadastro(erro=None):
    f.clear()
    print("Cadastro Corridinha".center(f.columns))

    f.texto_centralizado('Digite "q" no nome para voltar', -2)
    f.texto_centralizado("Email: ", 1)
    f.texto_centralizado("Senha: ", 2)

    if erro:
        f.texto_centralizado(erro, 4)

    nome = f.input_centralizado("Nome: ")

    if nome == "q":
        return tela_login()

    email = f.input_centralizado("Email: ", 1)

    senha = f.input_centralizado("Senha: ", 2)

    if not email or not senha or not nome:
        return cadastro("Email, senha ou nome inválidos!")

    if "@" not in email:
        return cadastro("Email inválido!")

    usuario = usuario_operacoes.ler_usuario(email)

    if usuario:
        return cadastro("Email já cadastrado!")
    else:
        return usuario_operacoes.adicionar_usuario(
            Usuario(nome, email, senha))


def tela_login():
    opcao = inicial()

    if opcao == "1":
        return login()
    elif opcao == "2":
        return cadastro()
    else:
        return tela_login()
