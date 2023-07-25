from time import sleep

print("\033[1;33mFALTAM 10 SEGUNDOS PARA VIRAR O ANO!\033[m")

for c in range(10, 0, -1):
    print(f"\033[1;33m{c}!\033[m")
    sleep(1)
print("FELIZ ANO NOVO!!")