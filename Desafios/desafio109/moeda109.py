"""
    DESAFIO 109:
    Modifique as funções criadas no desafio 107 para elas aceitarem um parâmetro a mais,
    informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""


def aumentar(num=0, taxa=0, formato=False):
    res = num + (num * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    res = num - (num * taxa/100)
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    res = num * 2
    return res if not formato else moeda(res)


def metade(num=0, formato=False):
    res = num / 2
    return res if not formato else moeda(res)


def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:>8.2f}".replace(".", ",")
