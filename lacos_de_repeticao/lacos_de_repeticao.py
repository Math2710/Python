# num = 1

# while (num <= 1):
#     print(num)
#     nume += 1
# print("Laço encerrado")

nome = None

while True:
    print('Digite seu nome, ou x para parar:')
    nome = input()

    if nome == 'x' or nome == 'k':
        break

    print(f'Bem-vindo, {nome}')