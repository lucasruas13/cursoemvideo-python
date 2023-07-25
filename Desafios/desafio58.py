from random import randint
from time import sleep

num_random = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Com quantos palpites você consegue acertar?")
acertou = False
cont = 0

while not acertou:
    num_user = int(input("Digite um número entre 0 e 10: "))
    print("Verificando....")
    sleep(1)
    cont += 1
    if 0 <= num_user <=10:
        if num_user == num_random:
            acertou = True
            print(f"Parabéns! Você acertou o número sorteado: {num_random}")
            print(f"Para acertar o número você precisou tentar {cont} vezes")
        else:
            if num_user < num_random:
                print("Mais.... Tente novamente.")
            else:
                print("Menos.... Tente novamente.")
    else:
        cont -= 1
        print("Valor inválido.")
