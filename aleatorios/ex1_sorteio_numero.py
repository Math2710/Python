import random
min = int(input("Digite o mínimo: "))
max = int(input("Digite o máximo: "))
print("------------------------------")
for n in range (1,6):
    aleatorio = random.randint(min, max)
    print(f"Sorteio {n}: {aleatorio}")