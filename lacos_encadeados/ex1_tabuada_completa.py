for tabuada in range (1,6):
    print(f"\nTabuada do {tabuada}")
    for multiplicador in range(1,11):
        resultado = multiplicador * tabuada
        print(f"{tabuada} x {multiplicador} = {resultado}")
        if multiplicador % 5 == 0:
            print("(múltiplo de 5 pulado)")
            continue
    


