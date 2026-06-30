vezes = 0
soma = 0
while True:
    numero = float(input("Digite um número (0 para parar): "))
    
    if (numero != 0):
        vezes += 1
        soma += numero
    else:
        if vezes > 0:
            media = soma / vezes
            print(f"Soma total: {soma} \nMédia {media:.2f}")
            break
        else:
            print("Nenhum número foi digitado.")
            break
     