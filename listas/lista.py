# ==================================================
# Aula de Python - Listas
# ==================================================
# Lista: representa uma sequência de valores.
# Sintaxe: nome_lista = [valores]
# ==================================================

# Criando listas
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]

# Concatenando listas
valores = n1 + n2

print("=== LISTA ORIGINAL ===")
print(f"Lista n1: {n1}")
print(f"Lista n2: {n2}")
print(f"Lista concatenada: {valores}")
print(f"Tipo da variável: {type(valores)}")

print("\n=== ACESSO E ALTERAÇÃO ===")
valores[0] = 9
print(f"Lista após alterar o primeiro valor: {valores}")
print(f"Penúltimo até o final: {valores[-2:]}")
print(f"Quantidade de elementos: {len(valores)}")

print("\n=== FUNÇÕES COM LISTAS ===")
print(f"Lista ordenada em ordem decrescente: {sorted(valores, reverse=True)}")
print(f"Soma dos valores: {sum(valores)}")
print(f"Menor valor: {min(valores)}")
print(f"Maior valor: {max(valores)}")

print("\n=== ADICIONANDO E REMOVENDO ELEMENTOS ===")
valores.append(13)
print(f"Após adicionar 13 no final: {valores}")

valores.pop()
print(f"Após remover o último elemento: {valores}")

valores.pop(3)
print(f"Após remover o elemento da posição 3: {valores}")

valores.insert(3, 21)
print(f"Após inserir 21 na posição 3: {valores}")

print("\n=== VERIFICANDO SE UM VALOR EXISTE NA LISTA ===")
print(f"O número 17 está na lista? {17 in valores}")

print("\n=== PERCORRENDO UMA LISTA COM FOR ===")
planetas = ["Mercúrio", "Vênus", "Marte", "Saturno", "Urano", "Netuno"]

for planeta in planetas:
    print(f"Planeta: {planeta}")