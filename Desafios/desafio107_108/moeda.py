"""
    DESAFIO 107:
    Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
    Faça também um programa que importe esse módulo e use algumas dessas funções.

    DESAFIO 108:
    Adapte o código do desafio #107, criando uma função adicional chamada moeda()
    que consiga mostrar os números como um valor monetário formatado.
"""


def aumentar(num=0, taxa=0):
    res = num + (num * taxa/100)
    return res


def diminuir(num=0, taxa=0):
    res = num - (num * taxa/100)
    return res


def dobro(num=0):
    res = num * 2
    return res


def metade(num=0):
    res = num / 2
    return res


def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:>8.2f}".replace(".", ",")
