"""
    DESAFIO 97:
    Faça um programa que tenha uma função chamada escreva(),
    que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def escreva(letra):
    # print((len(letra)+4) * "~")
    print(f"  {letra}")
    print((len(letra)+4) * "~")


# Programa Principal (def escreva):
escreva("don't sell")
escreva("yourself")
escreva("to fall")
escreva("in love")
