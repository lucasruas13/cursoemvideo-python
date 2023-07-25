"""
    DESAFIO 113:
    Reescreva a função leiaInt() que fizemos no desafio 104,
    incluindo agora a possibilidade da digitação de um número de tipo inválido.
    Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


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


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print("\033[0;31mERRO! O usuário não digitou o número inteiro.\033[m")
        else:
            return real


# Programa Principal (def leiaInt leiaFloat):
i = leiaInt("Digite um Inteiro: ")
f = leiaFloat("Digite um Real: ")
print(f"O valor inteiro foi {i} e o real foi {f}")
