telefone = input("Digite o número de telefone (formato: (XX) XXXXX-XXXX): ")

ddd = telefone[1:3]
numero = telefone[6:11]

print(f"O DDD é: {ddd}")
print(f"O número de telefone é: {numero}")


data = input("Digite a data de nascimento (formato: DD/MM/AAAA): ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")


email = input("Digite o endereço de e-mail (nome.escolaEAD@escola.org): ")
email_parts = email.split("@")
username = email_parts[0]
domain = email_parts[1] 
print(f"Nome de usuário: {username}")