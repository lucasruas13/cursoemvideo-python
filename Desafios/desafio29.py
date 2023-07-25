velocidade = int(input("Digite sua velocidade: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você está acima do limite permitido (80Km/h)! A sua multa vai custar = R$ {multa},00")
else:
    print(f"A sua velocidade está dentro do limite permitido (80Km/h)")