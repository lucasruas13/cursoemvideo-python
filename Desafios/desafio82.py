"""
    DESAFIO 82:
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, crie duas listas extras que vão conter apenas os valores
    pares e os valores ímpares digitados, respectivamente.
    Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
par = []
impar = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpares é {impar}")
