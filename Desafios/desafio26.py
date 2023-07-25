frase = input("Digite uma frase: ").lower().strip()

print("Quantas vezes a letra A aparece na frase: ", frase.count("a"))
print("A posição que o primeiro A aparece é: ", frase.find("a")+1)
print("A posição que o último A aparece é: ", frase.rfind("a")+1)