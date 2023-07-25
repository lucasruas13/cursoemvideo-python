print("x" * 40)
print("{:^40}".format("BANCO LITO'S"))
print("x" * 40)
valor = int(input("Quanto deseja sacar? "))
total = valor
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f"Total de {total_cedula} cédulas de R${cedula:.2f}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
