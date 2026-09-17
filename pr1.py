
# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno:Erik Rodrigues de Oliveira
# Data:17/09/2026
# Link do Repositório:
# ==============================================================================


dados_brutos = [
    "  Erik Rodrigues de Oliveira;Analista de Sistemas;46374638695  ",
    "  Matheus Moreira;Gerente de Projetos;91756483020  ",
    "  João Souza;Desenvolvedor;96850673000  ",
    "  Masqueiko de solza;comerciante de peixe;36472856748  ",

]


def limpar_e_formatar_texto(texto):
    texto = texto.strip()

    return texto


def extrair_codigo_ou_ddd(dado):
    dado = dado.strip()

    codigo = dado[0:2]

    return codigo


def processar_e_exibir_cadastros(lista_dados):
    total_processado = 0

    for dado in lista_dados:

        partes = dado.split(";")

        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]


        nome_formatado = limpar_e_formatar_texto(nome)
        cargo_formatado = limpar_e_formatar_texto(cargo)


        ddd = extrair_codigo_ou_ddd(telefone)


        print(f"Nome: {nome_formatado}")
        print(f"Cargo: {cargo_formatado}")
        print(f"DDD/Código: {ddd}")
        print("-" * 50)


        total_processado += 1


    return total_processado


def main():

    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print(f"\nTotal de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO")
    print("==================================================")


if __name__ == "__main__":
    main()