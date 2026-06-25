usuario = (input("Digite seu usuario: "))
senha = (input("Digite sua senha: "))
usuario_correto = "admin"
senha_correta = "1234"
bloqueado = False

if bloqueado:
    print("Conta bloqueada")

elif (usuario == usuario_correto) and (senha == senha_correta):
    print("Login bem sucedido")

elif (usuario != usuario_correto):
    print("Usuário não existe")

elif (senha != senha_correta):
    print("Senha incorreta")








