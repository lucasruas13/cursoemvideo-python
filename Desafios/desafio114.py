"""
    DESAFIO 114:
    Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print("Deu erro! Site inacessivel no momento.")
else:
    print("Tudo certo! Site acessivel no momento.")
    print("-" * 40)
    print(site.read())
