"""
    DESAFIO 94:
    Crie um programa que leia nome, sexo e idade de várias pessoas,
    guardando os dados de cada pessoa em um dicionárioe todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas
    B) A média de idade
    C) Uma lista com as mulheres
    D) Uma lista de pessoas com idade acima da média
"""

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa["nome"] = str(input("Nome: "))
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Favor digitar [M/F]")
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Favor digitar [S/N]")
    if resp == "N":
        break

print("-=" * 30)
print(f"A) Ao todo, temos {len(galera)} pessoas cadastradas.")

media = soma / len(galera)
print(f"B) A média de idade das pessoas é de {media:.1f} anos.")

print("C) As mulheres cadastradas foram: ", end="")
for p in galera:
    if p["sexo"] in "Ff":
        print(f"[{p['nome']}] ", end="")
print()

print(f"D) As pessoas que estão com a idade acima da média ({media:.1f}) são: ", end="")
for p in galera:
    if p["idade"] > media:
        print(f"[{p['nome']}] ", end="")
print()
print("-=" * 30)
