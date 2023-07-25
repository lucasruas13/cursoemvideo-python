print("\033[1;33m[ 1 ]\033[m \033[1;34msomar\033[m\n"
      "\033[1;33m[ 2 ]\033[m \033[1;34mmultiplicar\033[m\n"
      "\033[1;33m[ 3 ]\033[m \033[1;34mmaior\033[m\n"
      "\033[1;33m[ 4 ]\033[m \033[1;34mnovos números\033[m\n"
      "\033[1;33m[ 5 ]\033[m \033[1;34msair do programa\033[m\n")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operador = 1
maior = n1

if 1 <= operador <= 5:
    while operador != 5:
        operador = int(input("Digite o operador: "))
        if operador == 1:
            soma = n1 + n2
            print(f"Você escolheu o operador {operador}: somar.")
            print(f"{n1} + {n2} = {soma}")
        elif operador == 2:
            mult = n1 * n2
            print(f"Você escolheu o operador {operador}: multiplicar")
            print(f"{n1} * {n2} = {mult}")
        elif operador == 3:
            if n2 > n1:
                maior = n2
                print(f"Você escolheu o operador {operador}: maior")
                print(f"O número {n2} é maior que {n1}")
            else:
                print(f"Você escolheu o operador {operador}: maior")
                print(f"O número {n1} é maior que {n2}")
        elif operador == 4:
            print(f"Você escolheu o operador {operador}: novos números")
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
    if operador == 5:
        print(f"Você esclheu o operador {operador}: sair do programa.")
else:
    print("Operador inválido.")