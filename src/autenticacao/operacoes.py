import os
import shutil
from .. import ferramentas
from . import usuario

usuarios_caminho = "./data"
dados_usuario_caminho = "usuario.csv"


def adicionar_usuario(dados):
    caminho = f"{usuarios_caminho}/{dados.email}/"

    if os.path.exists(caminho + "usuario.csv"):
        return ler_usuario(dados.email)

    os.makedirs(caminho, exist_ok=True)

    arquivo = ferramentas.ler_csv(
        caminho + dados_usuario_caminho)

    atributos = ["nome", "email", "senha"]

    if len(arquivo) == 0:
        arquivo.append(atributos)

    novo_usuario = dados.__str__().split(", ")
    arquivo.append(novo_usuario)

    ferramentas.escrever_csv(caminho + dados_usuario_caminho, arquivo)

    return novo_usuario


def ler_usuario(email=None):
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


def atualizar_usuario(email, dados):
    caminho = f"{usuarios_caminho}/{email}/"

    if not ler_usuario(email):
        return None

    arquivo = ferramentas.ler_csv(caminho + dados_usuario_caminho)

    novo_usuario = dados.__str__().split(", ")
    arquivo[1] = novo_usuario

    ferramentas.escrever_csv(caminho + dados_usuario_caminho, arquivo)


def deletar_usuario(email):
    caminho = f"{usuarios_caminho}/{email}/"

    if os.path.exists(caminho):
        shutil.rmtree(caminho)
