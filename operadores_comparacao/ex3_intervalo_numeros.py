numero = int ((input)("Digite um número inteiro: "))

zero_a_10 = numero >= 0 and numero <= 10
onze_a_20 = numero >= 11 and numero <= 20
VinteUm_a_30 = numero >= 21 and numero <= 30
maior_que_30 = numero > 30

print(f"Está entre 0-10? {zero_a_10}")
print(f"Está entre 11-20? {onze_a_20}")
print(f"Está entre 21-30? {VinteUm_a_30}")
print(f"É maior que 30? {maior_que_30}")