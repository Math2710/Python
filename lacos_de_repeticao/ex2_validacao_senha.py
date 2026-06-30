senha_correta = "python123"
tentativas = 3

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado!")
        break
        
    else: 
        tentativas -= 1
        
        if tentativas > 0:
            print(f"Senha incorreta. Tentativas restantes: {tentativas}")
        else: 
            print("Acesso negado!")
            break

    

    

        

