import math
import random
import emoji

# Aula 8
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é: {raiz:.2f}")

num_random = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
print(emoji.emojize(f"O número aleatório gerado é: {num_random} :rooster:"))

# Aula 9
frase = "Curso em Vídeo Python"
print(frase[9:21:2])  # o 2 faz pular as letras de 2 em 2.
print(frase[:5])  # faz a contagem começar do 0 e ir até o 5.
print(frase[15:])  # faz a contagem começar do 15 e ir até o final.
print(frase[9::3])  # faz com que comece do 9 e pule de 3 em 3.
print(len(frase))  # len conta quantos caracteres possui na frase.
print(frase.count("o"))  # count conta quantas letras O tem na frase.
print(frase.count("o", 0, 13))  # conta quantas letras O possui entre as posições 0 e 13.
print(frase.find("deo"))  # mostra em qual posição começou a sequencia de letras 'deo'.
print(frase.find("Lucas"))  # quando coloca uma palavra que não possui na frase ele retorna a posição -1.
print("Curso" in frase)  # analise booleana (True/False) se possui uma palavra na frase.
print(frase.replace("Python", "Android"))  # troca a palavra Python por Android.
print(frase.upper())  # coloca todas as letras MAIÚSCULAS.
print(frase.lower())  # coloca todas as letras minúsculas.
print(frase.capitalize())  # coloca somente a primeira letra em MAIÚSCULA, as demais ficam minúsculas.
print(frase.title())  # coloca a primeira letra de todas as palavras MAIÚSCULAS.
print(frase.strip())  # remove todos os espaços inuteis (espaços no início e no fim) da frase.
print(frase.split())  # separa as palavras da frase em uma lista através do espaço (padrão) entre as mesmas.
print("-".join(frase))  # junta todas as letras da frase com um '-' entre elas.

print("""\nPrimeira cena, bom dia mundo
Eu, espírito e carne contra quase tudo
Pessoas fracas, fico puto
No meu sonho de liberdade elas são os muros
Na ilusão de pensar que eu vou cair na depressão
Mas eu não vou parar
Não tente me seguir
Mas se quiser tentar
O querer é poder, certamente
Pra quem sabe onde quer chegar""")  # colocar """ no início e no fim para armazenar textos dentro de um único PRINT.
