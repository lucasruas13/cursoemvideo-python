total = int(input("Quantos termos você deseja mostrar: "))
cont = 0
ultimo = 0
penultimo = 1
print(f"{ultimo} > ", end="")

while cont <= (total - 2):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    cont += 1
    print(f"{termo} > ", end="")
print("ACABOU")
