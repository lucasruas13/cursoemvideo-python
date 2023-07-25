s1 = float(input("Digite o primeiro segmento: "))
s2 = float(input("Digite o segundo segmento: "))
s3 = float(input("Digite o terceiro segmento: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Os segmentos digitados PODEM formar um triângulo.")
    if s1 == s2 == s3:
        print("Formam um triângulo EQUILÁTERO, pois todos os lados são iguais.")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("Formam um triângulo ISÓSCELES, pois dois lados são iguais.")
    elif s1 != s2 != s3 != s1:
        print("Formam um triângulo ESCALENO, pois todos os lados são diferentes.")
else:
    print("Os segmentos digitados NÃO PODEM formar um triângulo.")