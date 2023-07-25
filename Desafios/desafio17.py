from math import hypot

cat_oposto = float(input("Digite o tamanho do cateto oposto: "))
cat_adjacente = float(input("Digite o tamanho do cateto adjacente: "))
hipotenusa = hypot(cat_oposto, cat_adjacente)
print(f"O valor da hipotenusa é: {hipotenusa:.2f}")