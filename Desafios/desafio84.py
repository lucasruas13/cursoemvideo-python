"""
    DESAFIO 84:
    Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.
"""

lista = []
temp = []
maior = menor = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))

    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    lista.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break

print("-=" * 30)
print(f"Ao todo, você cadastrou {len(lista)} pessoas.")
print(f"O maior peso foi de {maior}Kg: ", end="")
for p in lista:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {menor}Kg: ", end="")
for p in lista:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
