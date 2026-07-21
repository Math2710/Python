import random

lista = {'Maçã', 'Banana', 'Uva', 'Pera', 'Manga', 'Abacaxi'}
sorteada = random.choice(lista)
sorteadas = random.sample(lista, 3)
embaralhada = random.shuffle(lista)

print(f"Lista original: {lista}")
print(f"Fruta sorteada: {sorteada}")
print(f"3 frutas sorteadas: {sorteadas}")
print(f"Lista embaralhada: {lista}")