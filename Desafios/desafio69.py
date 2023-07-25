mais_18 = homens = mulheres = mulheres_20 = 0

while True:
    idade = int(input("Digite uma idade: "))
    if idade >= 18:
        mais_18 += 1
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite um sexo [M/F]: ")).strip().upper()[0]
    if sexo in "M":
        homens += 1
    elif sexo in "F":
        mulheres += 1
    if sexo in "F" and idade < 20:
        mulheres_20 += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if continuar in "N":
        print("Obrigado por realizar nosso cadastro! FIM.")
        break
total = mulheres + homens
print(f"Foram cadastradas {total} pessoas!")
print(f"Maiores de 18 anos: {mais_18} pessoas")
print(f"Homens cadastrados: {homens} homens")
print(f"Mulheres com menos de 20 anos: {mulheres_20} mulheres")
