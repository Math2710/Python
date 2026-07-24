import random

listas = ['Mercúrio','Vênus','Marte','Saturno','Urano','Netuno']

for numero, planeta in enumerate(listas, start=1):
    print(f"{numero} - {planeta}")

print("------------------------------")

adicionar = input("Digite um planeta para adicionar: ")
adicionar = listas.append(adicionar)
remover = int (input("Digite um indice para remover: "))
remover = listas.pop(remover)

print(f"Lista final {listas}")
print(f"Plutão está na lista? {"Plutão" in listas}")