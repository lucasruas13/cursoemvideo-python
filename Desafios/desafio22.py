nome = input("Digite seu nome completo: ").strip()

print(f"Seu nome completo é: {nome}")
print("MAIÚSCULO: ", nome.upper())
print("MINUSCULO: ", nome.lower())
sem_espaco = nome.replace(" ", "")
print(f"Quantidade de letras do nome completo: {len(sem_espaco)} letras")
lista = nome.split()
print(f"Seu primeiro nome é {lista[0]} e ele possui {len(lista[0])} letras")