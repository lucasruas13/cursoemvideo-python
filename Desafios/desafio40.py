n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print(f"A sua média foi: {media:.1f}")

if media < 5.0:
    print("Você está \033[1;31mREPROVADO\033[m!")
elif media >= 7.0:
    print("Você está \033[1;32mAPROVADO\033[m!")
else:
    print("Você está de \033[1;33mRECUPERAÇÃO\033[m!")