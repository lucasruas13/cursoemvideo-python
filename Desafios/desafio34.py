salario = float(input("Digite seu salário: "))

if salario >= 0:
    if salario > 1250.00:
        aumento = salario * 0.1
    else:
        aumento = salario * 0.15
    print(f"Você ganhou um aumento de R$ {aumento:.2f}! Seu salário atualizado é R$ {(salario + aumento):.2f}")
else:
    print("Valor digitado inválido.")