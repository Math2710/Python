idade = int(input("Digite sua idade: "))
renda = float (input("Digite sua renda mensal: "))

votar = idade >= 18 
idoso = idade >= 60 
emprestimo = idade >= 21 and renda >= 2000 

msg_votar = "Pode votar: " + str (votar)
msg_idoso = "É idoso? " + str (idoso)
msg_emprestimo = "Pode pedir emprestimo? " + str (emprestimo)
print(msg_votar)
print(msg_emprestimo)
print(msg_idoso)
