"""
    DESAFIO 99:
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    O seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(*num):
    maior = cont = 0
    print("Analisando os valores passados...")
    sleep(1)
    for valor in num:
        print(f"[{valor}] ", end="")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")
    print("-=" * 30)


# Porgrama Principal (def maior):
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
