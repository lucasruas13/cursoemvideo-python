from datetime import date

ano = int(input("Digite um ano: "))

if ano == 0: # Se a pessoa digitar 0, o programa pegará o ano atual.
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO!")
else:
    print(f"O ano {ano} não é BISSEXTO!")