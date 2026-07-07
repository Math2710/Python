inicial =  int(input("DIgite um inicial:"))
final = int(input("DIgite um final:"))
for x in range(inicial, final, -1):
    if x % 3 == 0:
        print(f"Múltiplo de 3: {x}")
    else:
        print(x)
print("fogo!")