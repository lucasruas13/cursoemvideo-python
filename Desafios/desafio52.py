num = int(input("Digite um número inteiro: "))

if num > 1:
    for c in range(2, num):
        if num % c == 0:
            print(f"O número {num} NÃO É PRIMO.")
    else:
        print(f"O número {num} É PRIMO.")
else:
    print(f"Você digitou o número 1.")