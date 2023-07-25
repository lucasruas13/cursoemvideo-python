"""
    DESAFIO 79:
    Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
    Caso o número já exista lá dentro, ele não será adicionado.
    No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = []
while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("-=" * 30)
lista.sort()
print(f"Você digitou os valores {lista}")
