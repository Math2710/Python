numero = int (input("Digite um número inteiro: "))

while (numero > 0):
    numero -= 1
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
