"""
    DESAFIO 112:
    Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
    Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
    mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".")  # Converte o valor digitado para str e troca as vírgulas por ponto
        if entrada.isalpha() or entrada.strip() == "":  # Verifica se o valor digitado é numérico e se é um dado vazio
            print(f"\033[0;31mERRO: \"{entrada}\", é um preço inválido!\033[m")
        else:
            valido = True
            return float(entrada)
