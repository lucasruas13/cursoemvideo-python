soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma += c
print("Acima estão todos os números ímpares de 1 a 500 que são multiplos de 3.")
print(f"E a soma de todos eles são = {soma}")