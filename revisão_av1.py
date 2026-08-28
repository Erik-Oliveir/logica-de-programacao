def formatar_citação(nome_completo):
    partes = nome_completo.strip().split()
    sobrenome = partes[-1].upper()
    primeiro_nome = " ".join(partes[:-1])
    
    return sobrenome + ", " + primeiro_nome

if __name__ == "__main__":
    resultado1 = formatar_citação("Carlos Eduardo Andrade")
    print(resultado1)


def ano_ingresso():
    return 2022
cpf = "111.222.444-28"[0:4]
print(f"Alu-{ano_ingresso()}-{cpf}")
