from math import radians, sin, cos, tan

angulo = int(input("Digite o valor de um angulo: "))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))
print(f"O valor do SENO é {sen:.2f}, do COSSENO é {cos:.2f} e da TANGENTE é {tg:.2f}.")