num = [5, 2, 9, 1]
print(num)
print(f"Essa lista tem {len(num)} elementos")

num[2] = 3  # trocou o número 2 pelo 3
num.append(7)  # adicionando o número 7 no final da lista
num.insert(2, 0)  # adiciona o número 0 na posição 2 da lista
num.sort()  # colocando a lista em ordem crescente
num.sort(reverse=True)  # colocando a lista em ordem decrescente
num.pop()  # elimina o último número da lista
num.pop(2)  # elimina o elemento 2 da lista
num.remove(2)  # remove o primeiro número 2 da lista
valores = list(range(4, 11))  # cria uma lista em ordem crescente de 4 até 10

print(num)
print(f"Essa lista tem {len(num)} elementos")

if 4 in num:
    num.remove(4)
else:
    print("Não possui o número 4 na lista")

for cont, valor in enumerate(num):
    print(f"Na posição {cont} eu encontrei o valor {valor}")
print("Chegamos ao final da lista")

num2 = []
for c in range(0, 5):
    num2.append(int(input("Digite um número: ")))
print(num2)

a = [2, 3, 4, 7]
b = a[:]  # realiza uma cópia da lista A sem criar ligação entre as duas listas, ou seja, pode-se alterar
          # o valor de B sem ser alterado o valor de A.
b[2] = 8
print(f"Lista A: {a}")
print(f"Lista B: {b}")
