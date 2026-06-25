import random
sorteado1 = random.randint (1, 10)
sorteado2 = random.randint (1, 10)

ganhou = False

for tentativa in range(5):
    x = int (input("Advinhe um número de 1 a 10: "))
    y = int (input("Advinhe outro número de 1 a 10: "))


    if(sorteado1 == x and sorteado2 == y):
        print("Acertou os 2! Venceu!")
        ganhou = True
        break
    elif (x == sorteado1 or y == sorteado2):
        print("Você acertou um número!")
    else:
        print("Acertou nenhum! Tente novamente!")
if not ganhou:
    print(f"Game Over! Os números eram {sorteado1} e {sorteado2}")
