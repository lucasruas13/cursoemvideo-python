sinal = "S"
soma = cont = media = maior = menor = 0

while sinal in "Ss":
    num = int(input("Digite um número: "))
    sinal = input("Deseja continuar [S/N]: ").upper().strip()
    cont += 1
    soma += num
    media = soma / cont
    if cont == 1:
        menor = num
        maior = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
print(f"Menor valor digitado: {menor}\n"
      f"Maior valor digitado: {maior}\n"
      f"Média entre todos os números digitados: {media:.2f}")
