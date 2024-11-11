import random
from .. import ferramentas

def filtrar(dados: list[Registro], modo: str, valor) -> list[Registro]:
    """
    Filtra uma lista de registros de acordo com um atributo e valor especificados.

    A função percorre uma lista de objetos `Registro` e retorna uma nova lista contendo apenas os registros
    em que o atributo especificado pelo `modo` corresponde ao `valor` fornecido.

    Args:
        dados (list[Registro]): Lista de objetos `Registro` a ser filtrada.
        modo (str): Nome do atributo do registro pelo qual o filtro será aplicado (ex.: "tipo", "data", "distancia").
        valor: Valor que o atributo especificado deve ter para que o registro seja incluído no resultado.

    Returns:
        list[Registro]: Lista de registros filtrados que atendem ao critério especificado.

    Exemplo de uso:
        registros = [Registro("treino", "01/01/24", 5, 30, "Parque", "Ensolarado"),
                     Registro("competição", "02/01/24", 10, 60, "Estádio", "Nublado")]
        registros_filtrados = filtrar(registros, "tipo", "treino")
        # Retorna uma lista contendo apenas registros com "tipo" igual a "treino".
    """
    registros_filtrados: list[Registro] = []

    for registro in dados:
        if getattr(registro, modo) == valor:
            registros_filtrados.append(registro)

    return registros_filtrados

def ordenar_data(dados: list[Registro]) -> list[Registro]:
    """
    Ordena uma lista de registros com base na data em ordem cronológica.

    A função organiza uma lista de objetos `Registro` em ordem cronológica com base no atributo `data`.
    Cada data é convertida em um valor numérico para permitir a comparação, onde o cálculo considera 
    o dia, mês e ano para determinar a posição cronológica correta.

    Args:
        dados (list[Registro]): Lista de objetos `Registro` a ser ordenada pela data.

    Returns:
        list[Registro]: Lista de registros ordenados em ordem cronológica.

    Dependências:
        A função `data` no objeto `Registro` deve ser uma lista ou objeto com `dia`, `mes`, e `ano` como inteiros.

    Exemplo de uso:
        registros = [Registro("treino", "01/01/24", 5, 30, "Parque", "Ensolarado"),
                     Registro("competição", "02/01/23", 10, 60, "Estádio", "Nublado")]
        registros_ordenados = ordenar_data(registros)
        # Retorna a lista `registros` ordenada cronologicamente.
    """
    def ordenar(registro: Registro) -> int:
        data = registro.data  # Assumindo que `data` é um objeto `Data`
        dia = data.dia
        mes = data.mes
        ano = data.ano

        return dia + mes * 31 + ano * 372

    registros_ordenados: list[Registro] = sorted(dados, key=ordenar)

    return registros_ordenados

def sugerir_treino(dados: list[dict]) -> list:
    """
    Sugere um novo treino com base nas médias de distância e duração dos treinos anteriores.

    A função calcula a média das distâncias e durações dos registros fornecidos, em seguida adiciona um valor
    aleatório baseado em uma variação calculada para sugerir um treino personalizado. O treino sugerido é retornado
    com um formato específico, incluindo a data sugerida, a distância e a duração ajustadas aleatoriamente, 
    e outras informações fixas.

    Args:
        dados (list[dict]): Lista de registros de treinos anteriores, onde cada registro é um dicionário com chaves 
                             "distancia" (em km) e "duracao" (em minutos).

    Returns:
        list: Lista contendo os dados do treino sugerido no formato:
              [tipo, data sugerida, distância sugerida, duração sugerida, local, clima].

    Exemplo de uso:
        registros = [
            {"distancia": 5, "duracao": 30},
            {"distancia": 10, "duracao": 60},
            {"distancia": 7, "duracao": 45}
        ]
        treino_sugerido = sugerir_treino(registros)
        print(treino_sugerido)
    """
    media_dist = 0
    media_tempo = 0

    total = len(dados)

    # Cálculo das médias de distância e duração
    for registro in dados:
        media_dist += registro["distancia"]
        media_tempo += registro["duracao"]

    # Calculando as médias
    media_dist /= total
    media_tempo /= total

    # Calculando os deltas de variação para distâncias e durações
    delta_dist = int(media_dist / 5)
    delta_tempo = int(media_tempo / 5)

    # Gerando uma variação aleatória para a distância e duração sugeridas
    std_dist = random.randint(-delta_dist, delta_dist)
    std_tempo = random.randint(-delta_tempo, delta_tempo)

    # Retornando o treino sugerido
    return [
        "treino", 
        ferramentas.data(8, 10, 2024),  # Assumindo que `ferramentas.data` cria a data corretamente
        int(media_dist + std_dist),  # Distância sugerida ajustada
        int(media_tempo + std_tempo),  # Duração sugerida ajustada
        "Recife",  # Local do treino
        "Aberto"  # Clima do treino
    ]
