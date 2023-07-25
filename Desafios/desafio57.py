sexo = input("Digite seu sexo [M/F]: ").upper().strip()[0]
while sexo not in "MmFf":
    sexo = input("Ddos inválidos. Digite seu sexo [M/F]: ").upper().strip()[0]
print(f"Sexo {sexo} registrado com sucesso.")