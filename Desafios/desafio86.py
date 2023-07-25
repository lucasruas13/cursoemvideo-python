"""
    DESAFIO 86:
    Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
    No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição [{linha}, {coluna}]: "))
print("-=" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")  # :^6 é formatação de exibição para saltar 6 casas e centralizar
    print()
