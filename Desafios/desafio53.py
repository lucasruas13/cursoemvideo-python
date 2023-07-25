frase = input("Digite uma frase: ").replace(" ", "").lower()
if frase == frase[::-1]:
    print(f"A frase digitada é um palíndromo.")
else:
    print("A frase digitada NÃO é um palíndromo.")