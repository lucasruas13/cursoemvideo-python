"""
    DESAFIO 76:
    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25, "Transferidor", 4.2, "Compasso", 9.99,
            "Mochila", 120.32, "Canetas", 22.3, "Livro", 34.9)
print("=" * 37)
print("{:^37}".format("LISTAGEM DE PREÇOS"))
print("=" * 37)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    if pos % 2 != 0:
        print(f"{listagem[pos]:>7.2f}")
