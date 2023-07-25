membros = int(input("Quantidade de membros da família: "))
soma_idade = 0
mais_velho = 0
menos_20 = 0
for c in range(1, membros + 1):
    print(f"------- {c}ª PESSOA -------")
    nome = input("Digite seu nome: ").title().strip()
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ").upper().strip()
    soma_idade += idade
    if sexo == "M" and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if sexo == "F" and idade < 20:
        menos_20 += 1
media = soma_idade / membros
print(f"A média de idade do grupo é {media:.1f} anos.")
print(f"O homem mais velho da família é o {nome_velho} e ele tem {mais_velho} anos.")
print(f"Ao todo são {menos_20} mulheres com menos de 20 anos.")