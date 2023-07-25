pessoas = {"nome": "Lucas", "sexo": "M", "idade": 22}  # padrão de criação de um dicionário

print(pessoas["idade"])  # como exibir um elento específico de um dicionário
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e seu sexo é {pessoas["sexo"]}.')

print(pessoas.keys())  # como exibir as keys de cada dicionário
print(pessoas.values())  # como exibir os valores que contém dentro de um dicionário
print(pessoas.items())  # como exibir todos os elementos dentro de um dicionário

for k, v in pessoas.items():  # forma para exibir todos os elementos de um dicionário através do laço for
    print(f"{k} = {v}")

del pessoas["sexo"]  # como apagar uma key (sexo) dentro de um dicionário

pessoas["nome"] = "Lucas Gabriel"  # como alterar o valor de uma key (nome)
pessoas["peso"] = 74.5  # adicionando uma key + valor no dicionário
print(pessoas)

brasil = []  # lista
estado1 = {"uf": "Minas Gerais", "sigla": "MG"}
estado2 = {"uf": "Bahia", "sigla": "BA"}
brasil.append(estado1)  # adicionando um dicionário dentro de uma lista (brasil)
brasil.append(estado2)  # adicionando um dicionário dentro de uma lista (brasil)
print(brasil[1]["sigla"])  # forma de exibir especificando o valor a ser exibido

cidade = dict()  # dicionário
brasil = list()  # lista
for c in range(0, 3):
    cidade["cidade"] = str(input("Digite o nome da cidade: "))
    cidade["estado"] = str(input("Digite a sigla do estado da cidade: "))
    brasil.append(
        cidade.copy())  # adicionando dicionário em lista sem criar ligação (utiliza-se copy() ao invés de [:])
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}.")
