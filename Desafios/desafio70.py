total = mais_mil = cont = barato = 0
nome_barato = " "

while True:
    nome = str(input("Digite o nome do produto: ")).upper()
    preco = float(input("Digite o preço do produto: "))
    total += preco
    cont += 1
    if preco > 1000:
        mais_mil += 1
    if cont == 1:
        barato = preco
    else:
        if preco < barato:
            barato = preco
            nome_barato = nome
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if continuar in "N":
        print("Obrigado por comprar conosco!")
        break
print(f"Você realizou a compra de {cont} itens no valor total de R${total:.2f}")
print(f"Dos itens comprados, {mais_mil} custam mais de R$1000,00")
print(f"O item mais barato é o(a) {nome_barato} no valor de R${barato:.2f}")
