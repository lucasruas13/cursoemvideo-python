from random import randint

num_user = int(input("Digite um número entre 0 e 5: "))
num_random = randint(0, 5)
print(num_random)

if num_user >= 0 and 6 > num_user:
    if num_user == num_random:
        print(f"Parabéns! Você acertou o número sorteado: {num_random}")
    else:
        print(f"Não deu... você errou o número sorteado: {num_random}")
else:
    print("O número digitado é inválido.")