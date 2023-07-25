# TUPLAS SÃO IMUTÁVEIS!

lanche = ("hamburguer", "suco", "pizza", "pudim")  # criação de uma tupla

print(lanche[2])  # printar o elemento 2 da tupla (pizza)
print(lanche[0:2])  # printar 2 elementos começando do elemento 0 (hamburguer)
print(lanche[1:])  # printar do elemento 1 (suco) até o final
print(lanche[-1])  # printar o último elemento (pudim)
print(lanche[-2])  # printar o penultimo elemento (pizza)
print(len(lanche))  # printar quantos elementos tem na tupla (4)

for comida in lanche:
    print(f"Eu vou comer {comida}!")  # lê toda a tupla e imprime o elemento do momento da contagem
print("Comi todas as comidas da tupla!\n")

for cont in range(0, len(lanche)):  # outra forma de for para exibir os elementos de uma tupla
    print(f"Vou comer {lanche[cont]} na posição {cont}")

print(sorted(lanche))  # colocando uma tupla em ordem alfabetica
