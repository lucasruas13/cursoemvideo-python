primeiro = int(input("Digite o primeiro termo da contagem: "))
razao = int(input("Digite qual a razão de uma progressão aritmética: "))
ultimo = primeiro + 10 * razao

print(f"PROGRESSÃO ARITMÉTICA DO TERMO {primeiro} COM UMA RAZÃO DE {razao}:")
for c in range(primeiro, ultimo, razao):
    print(c, end='  >  ')
print("ACABOU!")
