"""
    DESAFIO 115:
    Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome
    e idade num arquivo de texto simples. O sistema só vai ter 2 opções:
    cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida.\033[m")
    sleep(1.5)
