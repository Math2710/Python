import random

numeros = []

for i in range(6):
    numero = random.randint(1, 50)
    numeros.append(numero)

print(f"Lista original: {numeros}")
print(f"Lista ordenada: {sorted(numeros)}")
print("------------------------------")
print(f"O número 25 está na lista? {25 in numeros}")
print(f"Soma: {sum(numeros)}")

media = sum(numeros) / len(numeros)

print(f"Média: {media:.2f}")