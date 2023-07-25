pessoas = [["Pedro", 25], ["Ana", 19], ["João", 32]]
print(pessoas)
print(pessoas[0][0])  # irá exibir o nome PEDRO
print(pessoas[1][1])  # irá exibir a idade 19
print(pessoas[2][0])  # irá exibir o nome JOÃO
print(pessoas[1])  # irá exibir a sub lista ["Ana", 19]
print()

for p in pessoas:
    print(f"{p[0]} tem {p[1]} anos de idade.")  # [0] representa o 1º elemento de cada sub lista (nomes)
                                                # [1] representa o 2º elemento de cada sub lista (idade)
print()

pessoas2 = []
dado = []
maior = menor = 0
for c in range(0, 4):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    pessoas2.append(dado[:])
    dado.clear()

for p2 in pessoas2:
    if p2[1] >= 18:
        print(f"{p2[0]} é maior de idade.")
        maior += 1
    else:
        print(f"{p2[0]} é menor de idade.")
        menor += 1
print(f"Temos {maior} maiores e {menor} menores de idade.")
