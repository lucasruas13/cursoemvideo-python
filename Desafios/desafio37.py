num = int(input("Digite um número inteiro: "))
print("- 1 para binário\n- 2 para octal\n- 3 para hexadecimal")
base = int(input("Escolha a base de 1-3: "))

if base == 1:
    binario = format(num, "b")
    print(f"O número {num} em binário é: {binario}")
elif base == 2:
    octal = format(num, "o")
    print(f"O número {num} em octal é: {octal}")
elif base == 3:
    hex = format(num, "X")
    print(f"O número {num} em hexadecimal é: {hex}")
else:
    print("O número digitado para base é inválido.")