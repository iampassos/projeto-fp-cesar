import os
import shutil
from .. import ferramentas
from .usuario import Usuario

usuarios_caminho = "./data"
dados_usuario_caminho = "usuario.csv"


def adicionar_usuario(dados: Usuario) -> Usuario:
    """
    Adiciona um novo usuário ao sistema.

    Argumentos:
        dados (Usuario): O objeto Usuario a ser adicionado.

    Retorna:
        Usuario: O usuário adicionado.

    Exemplo de uso:
        novo_usuario = adicionar_usuario(usuario_obj)
    """
    caminho = f"{usuarios_caminho}/{dados.email}/"

    if os.path.exists(caminho + "usuario.csv"):
        return ler_usuario(dados.email)

    os.makedirs(caminho, exist_ok=True)

    arquivo = ferramentas.ler_csv(caminho + dados_usuario_caminho)

    atributos = ["nome", "email", "senha"]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_usuario = dados.__str__().split(", ")
    arquivo.append(novo_usuario)

    ferramentas.escrever_csv(caminho + dados_usuario_caminho, arquivo)

    return novo_usuario


def ler_usuario(email: str | None = None) -> Usuario | list[Usuario] | None:
    """
    Lê um usuário ou todos os usuários registrados.

    Argumentos:
        email (str, opcional): O e-mail do usuário a ser lido.

    Retorna:
        Usuario | list[Usuario] | None: O usuário com o e-mail fornecido ou uma lista de todos os usuários, ou None caso não encontrado.

    Exemplo de uso:
        usuario = ler_usuario("email@example.com")
        todos_usuarios = ler_usuario()
    """
    usuarios = os.listdir(usuarios_caminho)

    if not email:
        resultados = []

        for i in usuarios:
            if i == ".gitkeep":
                continue

            dados = ferramentas.ler_csv(f"{usuarios_caminho}/{i}/usuario.csv")

            resultados.append(Usuario(*dados[0]))

        return resultados

    if email in usuarios:
        dados = ferramentas.ler_csv(
            f"{usuarios_caminho}/{email}/usuario.csv", False)

        if len(dados) == 0:
            return None

        return Usuario(*dados[0])


def atualizar_usuario(email: str, dados: Usuario) -> None:
    """
    Atualiza os dados de um usuário.

    Argumentos:
        email (str): O e-mail do usuário a ser atualizado.
        dados (Usuario): O novo objeto Usuario com os dados atualizados.

    Exemplo de uso:
        atualizar_usuario("email@example.com", usuario_atualizado)
    """
    caminho = f"{usuarios_caminho}/{email}/"

    if not ler_usuario(email):
        return None

    arquivo = ferramentas.ler_csv(caminho + dados_usuario_caminho)

    novo_usuario = dados.__str__().split(", ")
    arquivo[1] = novo_usuario

    ferramentas.escrever_csv(caminho + dados_usuario_caminho, arquivo)


def deletar_usuario(email: str) -> None:
    """
    Deleta um usuário do sistema.

    Argumentos:
        email (str): O e-mail do usuário a ser deletado.

    Exemplo de uso:
        deletar_usuario("email@example.com")
    """
    caminho = f"{usuarios_caminho}/{email}/"

    if os.path.exists(caminho):
        shutil.rmtree(caminho)
