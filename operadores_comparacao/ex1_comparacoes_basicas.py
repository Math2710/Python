numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

iguais = numero1 == numero2
diferentes = numero1 != numero2
maior = numero1 > numero2
menor = numero1 < numero2
maior_ou_igual = numero1 >= numero2
menor_ou_igual = numero1 <= numero2

print(f"{numero1} é igual a {numero2} = {iguais}")
print(f"{numero1} é diferente de {numero2} = {diferentes}")
print(f"{numero1} é maior que {numero2} = {maior}")
print(f"{numero1} é menor que {numero2} = {menor}")
print(f"{numero1} é maior ou igual a {numero2} = {maior_ou_igual}")
print(f"{numero1} é menor ou igual a {numero2} = {menor_ou_igual}")