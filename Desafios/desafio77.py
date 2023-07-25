"""
    DESAFIO 77:
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

tupla = ("BRASIL", "ARGENTINA", "CHILE", "ESTADOS UNIDOS",
         "EQUADOR", "PARAGUAI", "URUGUAI", "MEXICO",
         "VENEZUELA", "COLOMBIA", "PERU", "BOLIVIA")

for palavra in tupla:
    print(f"\nNa palavra {palavra} temos: ", end="")
    for letra in palavra:
        if letra.upper() in "AEIOU":
            print(letra, end=" - ")
