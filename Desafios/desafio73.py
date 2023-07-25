"""
    DESAFIO 73:
    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro, na ordem de colocação.
    Depois mostre:
    a) Os 5 primeiros times.
    b) Os últimos 4 colocados.
    c) Times em ordem alfabética.
    d) Em que posição está o time do Atlético-MG.
"""

tabela = ("Palmeiras", "Internacional", "Fluminense", "Flamengo", "Corinthians", "Athletico-PR", "Atletico-MG",
          "America-MG", "Goias", "Botafogo", "Santos", "Bragantino", "São Paulo", "Fortaleza", "Ceara", "Coritiba",
          "Avai", "Cuiaba", "Atletico-GO", "Juventude")
posicao_galo = tabela.index("Atletico-MG")

print("=" * 60)
print("TABELA DO BRASILEIRÃO:")
print(tabela)
print("=" * 60)
print("OS 5 PRIMEIROS COLOCADOS:")
print(tabela[:5])
print("=" * 60)
print("OS ÚLTIMOS 4 COLOCADOS:")
print(tabela[-4:])
print("=" * 60)
print("TABELA DOS TIMES EM ORDEM ALFABÉTICA:")
print(sorted(tabela))
print("=" * 60)
print(f"O GALO ESTÁ NA {posicao_galo + 1}ª POSIÇÃO DO BRASILEIRÃO")
print("=" * 60)
