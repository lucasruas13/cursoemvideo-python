from math import factorial

num = int(input("Digite um número para calcular seu fatorial: "))
cont = num
fat = 1

while cont > 0:
    print(cont, end="")
    print(" x " if cont > 1 else " = ", end="")
    fat *= cont
    cont -= 1
print(fat)


 # UTILIZANDO FOR
"""
for c in range(num, 0, -1):
    fat *= c
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
print(fat)
"""

 # UTILIZANDO MATH (FACTORIAL)
"""
# fatorial_math = factorial(num)
# print(f"O fatorial (utilizando MATH) de {num}! é {fatorial_math}")
"""