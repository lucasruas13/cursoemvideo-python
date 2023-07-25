from random import choice
from time import sleep

user = input("Escolha > PEDRA - PAPEL - TESOURA: ").upper()
itens = ["PEDRA", "PAPEL", "TESOURA"]
pc = choice(itens)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(1)
print(f"PC ESCOLHEU: {pc}")

if user == pc:
    print(f"\033[1;33mEMPATE\033[m! Ambos escolheram {user}.")
elif user == "PEDRA" and pc == "TESOURA":
    print(f"\033[1;32mVOCÊ VENCEU\033[m! {user} vence {pc}.")
elif user == "TESOURA" and pc == "PAPEL":
    print(f"\033[1;32mVOCÊ VENCEU\033[m! {user} vence {pc}.")
elif user == "PAPEL" and pc == "PEDRA":
    print(f"\033[1;32mVOCÊ VENCEU\033[m! {user} vence {pc}.")
elif pc == "PEDRA" and user == "TESOURA":
    print(f"\033[1;31mPC VENCEU\033[m! {pc} vence {user}.")
elif pc == "TESOURA" and user == "PAPEL":
    print(f"\033[1;31mPC VENCEU\033[m! {pc} vence {user}.")
elif pc == "PAPEL" and user == "PEDRA":
    print(f"\033[1;31mPC VENCEU\033[m! {pc} vence {user}.")
else:
    print("\033[1;31mOpção digitada INVÁLIDA!\033[m")