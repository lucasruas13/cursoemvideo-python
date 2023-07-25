num = soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    soma += num
print(f"A soma dos números digitados foi {soma}")


for c in range(0, 10, 3):
    print(c)
