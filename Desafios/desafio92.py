"""
    DESAFIO 92:
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
    Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

pessoa = dict()
pessoa["nome"] = str(input("Nome: "))
ano = int(input("Ano de Nascimento: "))
pessoa["idade"] = datetime.now().year - ano
pessoa["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))

if pessoa["ctps"] == 0:
    print("-=" * 30)
    print(pessoa)
    for k, v in pessoa.items():
        print(f"{k} tem o valor {v}")
else:
    pessoa["contratação"] = int(input("Ano de Contratação: "))
    pessoa["salário"] = float(input("Salário: R$ "))
    pessoa["aposentadoria"] = (pessoa["contratação"] + 35) - ano
    print("-=" * 30)
    print(pessoa)
    for k, v in pessoa.items():
        print(f"{k} tem o valor {v}")
