"""
    DESAFIO 98:
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
    início, fim e passo. O seu programa tem que realizar três contagens através da função criada:
    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada
"""
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("-=" * 30)
    print(f"Contagem de {i} até {f} de {p} em {p}:")
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="")
            cont += p
            sleep(0.5)
        print("    FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="")
            cont -= p
            sleep(0.5)
        print("    FIM!")


# Programa Principal (def contador):
contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
