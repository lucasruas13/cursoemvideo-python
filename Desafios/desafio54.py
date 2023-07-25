from datetime import date

maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input("Digite o seu ano de nascimento: "))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f"Número de pessoas maiores de idade: {maior}")
print(f"Número de pessoas menores de idade: {menor}")