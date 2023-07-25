from datetime import date

ano = int(input("Qual seu ano de nascimento? "))
idade = date.today().year - ano
print(f"Sua idade é: {idade} anos")

if idade > 18:
    print(f"Você já passou do período de alistamento em {idade - 18} anos!!")
elif idade < 18:
    print(f"Você ainda não chegou no período de alistamento! Faltam {18 - idade} anos para se alistar.")
else:
    print(f"Você está com {idade} anos e deve se alistar agora!")