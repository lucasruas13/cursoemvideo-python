from random import randint

print("VAMOS JOGAR PAR OU IMPAR")
vitoria = 0

while True:
    escolha_user = " "
    while escolha_user not in "PI":
        escolha_user = str(input("PAR ou IMPAR [P/I]: ")).strip().upper()[0]
    num_user = int(input("Jogue um número: "))
    num_pc = randint(0, 10)
    total = num_user + num_pc
    print(f"Você jogou {num_user} e o computador jogou {num_pc}. O total deu: {total} ", end="")
    print(f"(PAR)" if total % 2 == 0 else "(IMPAR)")
    if escolha_user in "P":
        if total % 2 == 0:
            print("PARABÉNS! Você venceu. Vamos jogar novamente.")
            vitoria += 1
        else:
            print("GAME OVER! Você perdeu.")
            break
    if escolha_user in "I":
        if total % 2 == 1:
            print("PARABÉNS! Você venceu. Vamos jogar novamente.")
            vitoria += 1
        else:
            print("GAME OVER! Você perdeu.")
            break
print(f"Você conseguiu vencer o computador {vitoria} vezes. Até a próxima!")
