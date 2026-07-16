import random


for conjunto in range(1,4):
    soma = 0
    print(f"\nConjunto {conjunto}:")
    for aleatorio in range(1,6):
        num = random.randint(1, 100)
        if num % 2 == 0:
            soma += num
            print(f"{num} -> par")
        else:
            print(f"{num} -> ímpar")
    print(f"Soma dos pares do {conjunto}: {soma}")
        