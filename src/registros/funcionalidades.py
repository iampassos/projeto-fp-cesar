from .registro import Registro


def filtrar(dados: list[Registro], modo: str, valor) -> list[Registro]:
    registros_filtrados = []

    for i in dados:
        if getattr(i, modo) == valor:
            registros_filtrados.append(i)

    return registros_filtrados


def filtrar_mes(dados: list[Registro], mes: int, ano: int) -> list[Registro]:
    filtrados = []

    for i in dados:
        if i.data.mes == mes and i.data.ano == ano:
            filtrados.append(i)

    return filtrados


def ordenar_data(dados: list[Registro]) -> list[Registro]:
    def ordenar(dado: Registro):
        data = dado.data
        dia = data.dia
        mes = data.mes
        ano = data.ano

        return dia + mes * 31 + ano * 372

    registros_ordenados = sorted(dados, key=ordenar)

    return registros_ordenados
