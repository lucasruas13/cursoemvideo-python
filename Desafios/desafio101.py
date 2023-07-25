"""
    DESAFIO 101:
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
    ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
    OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f"Com {idade} anos: NÃO VOTA.")
    elif 16 <= idade < 18 or idade > 65:
        print(f"Com {idade} anos: VOTO OPCIONAL.")
    else:
        print(f"Com {idade} anos: VOTO OBRIGATÓRIO.")

# Programa Principal (def voto):
while True:
    nasc = int(input("Em que ano você nasceu? "))
    print(voto(nasc))
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("Favor digitar [S/N]")
    if resp == "N":
        break
