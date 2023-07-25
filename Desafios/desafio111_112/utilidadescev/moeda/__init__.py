"""
    DESAFIO 111:
    Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
    Transfira todas as funções utilizadas nos desafios 107, 108 e 109
    para o primeiro pacote e mantenha tudo funcionando.
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


def resumo(num=0, taxaa=0, taxad=0):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(num)}")
    print(f"Dobro do preço: \t{dobro(num, True)}")
    print(f"Metade do preço: \t{metade(num, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(num, taxaa, True)}")
    print(f"{taxad}% de redução: \t{diminuir(num, taxad, True)}")
    print("-" * 30)
