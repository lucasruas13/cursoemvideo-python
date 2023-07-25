from datetime import date

print("\033[4;44m CONFEDERAÇÃO NACIONAL DE NATAÇÃO \033[m")
ano = int(input("Digite o seu ano de nascimento: "))
idade = date.today().year - ano

if idade <= 9:
    print(f"Você tem {idade} anos e a sua categoria é \033[1;33mMIRIM\033[m!")
elif idade > 9 and idade <= 14:
    print(f"Você tem {idade} anos e a sua categoria é \033[1;33mINFANTIL\033[m!")
elif idade > 14 and idade <= 19:
    print(f"Você tem {idade} anos e a sua categoria é \033[1;33mJUNIOR\033[m!")
elif idade == 20:
    print(f"Você tem {idade} anos e a sua categoria é \033[1;33mSÊNIOR\033[m!")
else:
    print(f"Você tem {idade} anos e a sua categoria é \033[1;33mMASTER\033[m!")