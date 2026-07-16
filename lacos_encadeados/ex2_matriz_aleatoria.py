import random
for linhas in range (1,4):
    for colunas in range (1,5):
        num = random.randint(1, 50)
        print(f"{num:<4}", end="")
    print()

