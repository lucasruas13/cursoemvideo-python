"""
    DESAFIO 81:
    Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"Foram digitados {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 not in lista:
    print("O número 5 não foi digitado, portanto não se encontra na lista...")
else:
    print("O número 5 foi digitado e está na lista!")
