a = int (input("Digite um número inteiro: "))
b = int (input("Digite outro número inteiro: "))
c = int (input("Digite mais um número inteiro: "))

calculo1 = (a + b) * c 
calculo2 = (a * b) + c 
calculo3 = a ** b * c 
calculo4 = (a + b) / c 

print(f"({a} + {b}) * {c} = {calculo1}")
print(f"({a} * {b}) + {c} = {calculo2}")
print(f"({a} eleavdo a {b}) * {c} = {calculo3}")
print(f"({a} + {b}) divido por {c} = {calculo4}")