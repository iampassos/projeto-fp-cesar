def filtrar(dados, modo, valor):
    registros_filtrados = []

    for dado in dados:
        if getattr(dado, modo) == valor:
            registros_filtrados.append(dado)

    return registros_filtrados


def filtrar_mes(dados, mes, ano):
    filtrados = []

    for i in dados:
        if i.data.mes == mes and i.data.ano == ano:
            filtrados.append(i)

    return filtrados


def ordenar_data(dados):
    def ordenar(dado):
        data = dado.data
        dia = data.dia
        mes = data.mes
        ano = data.ano

        return dia + mes * 31 + ano * 372

    registros_ordenados = sorted(dados, key=ordenar)

    return registros_ordenados
