def soma(a, b):
    """
    -> função criada para somar dois números
    :param a: primeiro número da soma
    :param b: segundo número da soma
    :return: total da soma entre os 2 números
    """
    s = a + b
    print(f"    {a} + {b} = {s}")
    print("--" * 10)


# Programa Principal (def soma):
help(soma)  # comando utilizado para chamar a instrução descrita acima
soma(4, 5)
soma(6, 7)
soma(8, 9)


def contador(*num):  # forma de criar uma função sem declarar o tamanho finito de valores que irá receber
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números.")
    print("--" * 10)


# Programa Principal (def contador):
contador(2, 1, 7)
contador(3, 7)
contador(10, 2, 0, 5)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa Principal (def dobra):
valores = [6, 3, 9, 1, 0, 2]
print(f"Os valores iniciais foram: {valores}")
dobra(valores)
print(f"Os valores iniciais ao dobro são: {valores}")
