while True:
    num = int(input("Digite um número para saber a tabuada: "))
    if num < 0:
        print("PROGRAMA ENCERRADO. Volte sempre!")
        break
    for c in range(0, 11):
        tab = c * num
        print(f"{num} x {c} = {tab}")
