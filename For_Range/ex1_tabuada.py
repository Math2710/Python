numero = int(input("Digite um número: "))

# resultado = numero * tabuada

for num in range(1,10,1):
    if num == 5:
        continue
    resultado = numero * num
    print(f"{numero} x {num} = {resultado}" )