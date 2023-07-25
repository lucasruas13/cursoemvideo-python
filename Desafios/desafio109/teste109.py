import moeda109

n = float(input("Digite o preço: R$ "))
print(f"A metade de {moeda109.moeda(n)} é {moeda109.metade(n, True)}")
print(f"O dobro de {moeda109.moeda(n)} é {moeda109.dobro(n, True)}")
print(f"Aumentando 10%, temos {moeda109.aumentar(n, 10, True)}")
print(f"Diminuindo 20%, temos {moeda109.diminuir(n, 20, True)}")
