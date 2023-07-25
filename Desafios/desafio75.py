"""
    DESAFIO 75:
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
"""

tupla = (int(input("Digite um número: ")),
         int(input("Digite outro número: ")),
         int(input("Digite mais um número: ")),
         int(input("Digite o último número: ")))

print(f"Você digitou os números {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 not in tupla:
    print("O valor 3 não foi digitado em nenhuma posição")
else:
    print(f"O valor 3 apareceu na {tupla.index(3)+1}ª posição")
print("Os valores pares digitados foram: ", end="")
for n in tupla:
    if n % 2 == 0:
        print(n, end="  ")
