import random
print("------------------------------")
for rodada in range(1,4):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print(f"Rodada: {rodada} Dado 1 = {dado1} | Dado 2 = {dado2} | Soma = {soma}" )
    