from .registro import Registro


def filtrar(dados: list[Registro], modo: str, valor) -> list[Registro]:
    """
    Filtra uma lista de registros com base em um atributo e valor específicos.

    Argumentos:
        dados (list[Registro]): A lista de registros a ser filtrada.
        modo (str): O atributo a ser utilizado para filtrar os registros.
        valor: O valor que o atributo deve ter para o filtro.

    Retorna:
        list[Registro]: A lista de registros filtrados.

    Exemplo de uso:
        registros_filtrados = filtrar(dados, 'tipo', 'corrida')
    """
    registros_filtrados = []

    for i in dados:
        if getattr(i, modo) == valor:
            registros_filtrados.append(i)

    return registros_filtrados


def filtrar_mes(dados: list[Registro], mes: int, ano: int) -> list[Registro]:
    """
    Filtra uma lista de registros por mês e ano.

    Argumentos:
        dados (list[Registro]): A lista de registros a ser filtrada.
        mes (int): O mês a ser considerado para o filtro.
        ano (int): O ano a ser considerado para o filtro.

    Retorna:
        list[Registro]: A lista de registros filtrados pelo mês e ano.

    Exemplo de uso:
        registros_filtrados = filtrar_mes(dados, 10, 2024)
    """
    filtrados = []

    for i in dados:
        if i.data.mes == mes and i.data.ano == ano:
            filtrados.append(i)

    return filtrados


def ordenar_data(dados: list[Registro]) -> list[Registro]:
    """
    Ordena uma lista de registros por data (dia, mês, ano).

    Argumentos:
        dados (list[Registro]): A lista de registros a ser ordenada.

    Retorna:
        list[Registro]: A lista de registros ordenados por data.

    Exemplo de uso:
        registros_ordenados = ordenar_data(dados)
    """
    def ordenar(dado: Registro):
        data = dado.data
        dia = data.dia
        mes = data.mes
        ano = data.ano

        return dia + mes * 31 + ano * 372

    registros_ordenados = sorted(dados, key=ordenar)

    return registros_ordenados
