numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
resto_da_divisao = numero1 % numero2

print (f"{numero1} + {numero2} = {soma:.2f}")
print (f"{numero1} - {numero2} = {subtracao:.2f}")
print (f"{numero1} * {numero2} = {multiplicacao:.2f}")
print (f"{numero1} dividido por {numero2} = {divisao:.2f}")
print (f"A divisão inteira de {numero1} por {numero2} = {divisao_inteira}")
print (f"A sobra de {numero1} dividido por {numero2} = {resto_da_divisao}")
