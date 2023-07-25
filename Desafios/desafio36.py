casa = float(input("Qual o valor da casa que você deseja comprar? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos você deseja pagar a casa? "))
limite_mes = salario * 0.3
prestacao = casa / (anos * 12)

if prestacao <= limite_mes:
    print("Parabéns! Você pode comprar esta casa!")
    print(f"O valor da casa de R${casa:.2f} será pago em {casa / limite_mes:.0f} meses por uma prestação de R${limite_mes:.2f} ao mês.")

else:
    print("Infelizmente você não pode comprar esta casa...")
    print(f"O valor da prestação de R${prestacao:.2f} é superior ao limite de 30% do seu salário (R${limite_mes:.2f})")