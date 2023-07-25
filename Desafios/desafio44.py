valor = float(input("Digite o valor do produto: "))
print("- 1: à vista \033[1;34mdinheiro/cheque\033[m: \033[1;33m10%\033[m de desconto.\n"
      "- 2: à vista no \033[1;34mcartão\033[m: \033[1;33m5%\033[m de desconto.\n"
      "- 3: em até \033[1;34m2x no cartão\033[m: preço normal.\n"
      "- 4: \033[1;34m3x ou mais\033[m no cartão: \033[1;33m20%\033[m de juros.\n")
pagamento = int(input("Digite o tipo de pagamento entre 1-4: "))

if pagamento == 1:
    total = valor * 0.9
    print(f"O valor à pagar com os 10% de desconto é R${total:.2f}")
elif pagamento == 2:
    total = valor * 0.95
    print(f"O valor à pagar com os 5% de desconto é R${total:.2f}")
elif pagamento == 3:
    print(f"O valor à pagar com até 2x no cartão sem juros é R${valor:.2f}")
elif pagamento == 4:
    total = valor * 1.2
    print(f"O valor à pagar com os 20% de juros é R${total:.2f}")
else:
    print("Tipo de pagamento inválido.")