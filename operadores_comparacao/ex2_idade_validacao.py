idade = int (input("Digite sua idade: "))

maior_de_idade = idade >= 18
menor_de_idade = idade < 18
pode_tirar_cnh = idade >= 18
aposentado = idade >= 65

print(f"É maior de idade? {maior_de_idade}")
print(f"É menor de idade? {menor_de_idade}")
print(f"Pode tirar a carteira? {pode_tirar_cnh}")
print(f"É aposentado? {aposentado}")

