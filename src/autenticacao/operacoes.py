import os
import shutil
from .. import ferramentas
from . import usuario

usuarios_caminho: str = "./data"
dados_usuario_caminho = "usuario.csv"


def adicionar_usuario(dados: usuario.Usuario):
    caminho = f"{usuarios_caminho}/{dados.email}/"

    if os.path.exists(caminho + "usuario.csv"):
        return ler_usuario(dados.email)

    os.makedirs(caminho, exist_ok=True)

    arquivo: list[list[str]] = ferramentas.ler_csv(
        caminho + dados_usuario_caminho)

    atributos: list[str] = ["nome", "email", "senha"]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_usuario: list[str] = dados.__str__().split(", ")
    arquivo.append(novo_usuario)

    ferramentas.escrever_csv(caminho + dados_usuario_caminho, arquivo)

    return novo_usuario


def ler_usuario(email: str = None):
    usuarios = os.listdir(usuarios_caminho)

    if not email:
        resultados = []

        for i in usuarios:
            if i == ".gitkeep":
                continue

            dados = ferramentas.ler_csv(
                f"{usuarios_caminho}/{i}/usuario.csv")

            resultados.append(usuario.Usuario(*dados[0]))

        return resultados

    if email in usuarios:
        dados = ferramentas.ler_csv(
            f"{usuarios_caminho}/{email}/usuario.csv", False)

        if len(dados) == 0:
            return None

        return usuario.Usuario(*dados[0])


def atualizar_usuario(email: str, dados: usuario.Usuario):
    caminho = f"{usuarios_caminho}/{email}/"

    if not ler_usuario(email):
        return None

    arquivo = ferramentas.ler_csv(caminho + dados_usuario_caminho)
    arquivo[0] = ["nome", "email", "senha"]

    novo_usuario: list[str] = dados.__str__().split(", ")
    arquivo.append(novo_usuario)

    ferramentas.escrever_csv(caminho + dados_usuario_caminho, arquivo)

    return novo_usuario


def deletar_usuario(email: str) -> None:
    caminho = f"{usuarios_caminho}/{email}/"

    if os.path.exists(caminho):
        shutil.rmtree(caminho)
