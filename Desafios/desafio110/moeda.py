"""
    DESAFIO 110:
    Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
    que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
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
