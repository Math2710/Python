n1 = int (input ("Digite o primeiro número inteiro: "))
n2  = int (input ("Digite o segundo número inteiro: "))

soma = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2

print(f"A soma de {n1} + {n2} é {soma} | Tipo: {type(soma)}")
print(f"A subtração de {n1} por {n2} é {subtração} | Tipo: {type(subtração)}")
print(f"A multiplicação de {n1} vezes {n2} é {multiplicação} | Tipo: {type(multiplicação)}")
print(f"A divisão de {n1} por {n2} é {divisão:.2f} | Tipo: {type(divisão)}")