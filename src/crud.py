import ferramentas

treinoCaminho = "./data/treinos.csv"

# Adicionar um treino/competição ao banco de dados
# Formato: (A ordem importa)
# {
#     "tipo": "",
#     "data": "",
#     "distancia": "",
#     "duracao": "",
#     "localizacao": "",
#     "clima": "",
# }


def addTreino(dados):
    arquivo = ferramentas.lerCSV(treinoCaminho)

    arquivo[0] = ["tipo", "data", "distancia",
                  "duracao", "localizacao", "clima"]

    novoTreino = ",".join(str(valor) for valor in dados.values()).split(",")
    arquivo.append(novoTreino)

    ferramentas.escreverCSV(treinoCaminho, arquivo)

