primeiro = int(input("Digite o primeiro termo da contagem: "))
razao = int(input("Digite qual a razão da progressão aritmética: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo}  >  ", end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("FIM!")
print(f"Progressão finalizada com {total} termos mostrados.")
