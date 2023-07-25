numero = int(input("Informe um número entre 1 e 9999: "))

if numero > 0 and numero < 10000:
    u = numero // 1 % 10
    d = numero // 10 % 10
    c = numero // 100 % 10
    m = numero // 1000 % 10
    print(f"Analisando o número {numero}...")
    print(f"Unidade: {u}")
    print(f"Dezena: {d}")
    print(f"Centena: {c}")
    print(f"Milhar: {m}")
else:
    print(f"O número {numero} é inválido.")