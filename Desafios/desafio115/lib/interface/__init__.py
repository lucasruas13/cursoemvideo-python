def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;31mERRO! O usuário não digitou o número inteiro.\033[m")
        else:
            return inteiro


def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[32mSua opção: \033[m")
    return opc
