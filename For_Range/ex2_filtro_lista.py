Lista = [3, 8, 15, 4, 7, 12, 9, 6]
encontrados = 0
media = 0
soma = 0
for numero in Lista:
  if numero % 2 == 0:
    encontrados +=1
    soma += numero
    



media = soma / encontrados

print(f"Quantidade de pares: {encontrados}")
print(f"Soma do pares: {soma}")
print(f"Média dos pares: {media}")