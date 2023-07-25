cidade = input("Digite o nome da sua cidade: ").title()
lista = cidade.split()

if "Santo" in lista[0]:
    print(f"O nome da sua cidade é {cidade} e ela começa com SANTO.")
else:
    print(f"O nome da sua cidade é {cidade} e ela não começa com SANTO.")