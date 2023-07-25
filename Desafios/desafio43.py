peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.1f}")

if imc < 18.5:
    print("Você está \033[1;33mabaixo do peso\033[m.")
elif imc >= 18.5 and imc <= 24.9:
    print("Você está no \033[1;32mpeso ideal\033[m.")
elif imc >= 25 and imc <= 29.9:
    print("Você está com \033[1;33msobrepeso\033[m.")
elif imc >= 30 and imc <= 39.9:
    print("Você está com \033[1;31mobesidade\033[m.")
else:
    print("Você está com \033[1;31mobesidade mórbida\033[m.")