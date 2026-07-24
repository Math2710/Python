notas = list()
qtd = 0
while True:
    nota = float(input("Digite uma nota (-1 para parar):"))
    if(nota == -1):
        break
    else:
        notas.append(nota)
        qtd +=1
total = sum(notas)
media = total / qtd
print(f"Notas: {notas}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
print(f"Média: {media:.2f}")
if(media >= 7):
    print("Resultado: Aprovado")
else: 
    print("Resultado: Reprovado")