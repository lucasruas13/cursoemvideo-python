km = int(input("Digite a distância da sua viagem em Km: "))

if km >= 0:
    if km <= 200:
        valor = km * 0.50
    else:
        valor = km * 0.45
    print(f"A distância da sua viagem é {km}Km e o valor da passagem é R$ {valor:.2f}")
else:
    print("Distância inválida!")