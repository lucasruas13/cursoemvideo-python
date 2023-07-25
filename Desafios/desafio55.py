maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input("Digite o seu peso em Kg: "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso digitado foi {maior:.1f} Kg")
print(f"O menor peso digitado foi {menor:.1f} Kg")