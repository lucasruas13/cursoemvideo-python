"""
    DESAFIO 80:
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
    já na posição correta de inserção (sem usar o sort()).
    No final, mostre a lista ordenada na tela.
"""

lista = []
for c in range(0, 5):
    num = int(input("Digite um valor: "))
    if c == 0:
        lista.append(num)
        print("Adicionado no final da lista...")
    elif num > lista[-1]:  # se num for maior que o último valor
        lista.append(num)
        print("Adicionado no final da lista...")
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f"Adicionado na posição {posicao} da lista...")
                break
            posicao += 1
print("-=" * 30)
print(f"Os valores digitados em ordem foram {lista}")
