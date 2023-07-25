"""
    DESAFIO 87:
    Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_col = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}, {coluna}]: "))
print("-=" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")  # :^6 é formatação de exibição para saltar 6 casas e centralizar
        if matriz[linha][coluna] % 2 == 0:  # if para separar e somar os números pares da matriz
            soma_par += matriz[linha][coluna]
    print()
print("-=" * 30)
print(f"A soma dos valores pares é {soma_par}.")
for linha in range(0, 3):  # for para separar e somar os números da 3ª coluna
    soma_col += matriz[linha][2]
print(f"A soma dos valores da 3ª coluna é {soma_col}.")
for coluna in range(0, 3):  # for e if para verificar qual número da 2ª linha é o maior
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f"O maior valor da 2ª linha é {maior}.")
