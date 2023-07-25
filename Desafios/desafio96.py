"""
    DESAFIO 96:
    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
    retangular (largura e comprimento) e mostre a área do terreno.
"""


def area(l, c):
    a = l * c
    print(f"A área de um terreno {l} x {c} é de {a}m².")


# Programa Principal (def area):
print("Controle de Terrenos")
print("-=" * 15)
largura = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))
area(largura, comp)
