TAXA_PROCESSAMENTO = 2.00


def calcular_frete(valor_compra, peso_kg):
    frete = peso_kg * 5

    if valor_compra >= 200:
        frete = frete * 0.50

    return frete


print("=== CALCULADORA DE FRETE ===")

valor_compra = float(input("Digite o valor da compra: R$ "))
peso_kg = float(input("Digite o peso da encomenda (kg): "))

frete = calcular_frete(valor_compra, peso_kg)

print(f"Frete final: R$ {frete:.2f}")

def aplicar_cupom(valor_item, cupom_desconto):
    valor_com_desconto = valor_item - (valor_item * cupom_desconto / 100)
    valor_final = valor_com_desconto + TAXA_PROCESSAMENTO

    return valor_final


print("\n=== SISTEMA DE CUPOM ===")

valor_item = float(input("Digite o valor do item: R$ "))
cupom_desconto = float(input("Digite o desconto do cupom (%): "))

preco_final = aplicar_cupom(valor_item, cupom_desconto)

print(f"Preço final com desconto e taxa: R$ {preco_final:.2f}")

def exibir_cronograma_regressivo(parcelas_restantes, valor_parcela):
    if parcelas_restantes == 0:
        print("Todas as parcelas foram quitadas!")
        return

    print(f"Restam {parcelas_restantes} parcela(s) de R$ {valor_parcela:.2f}")

    exibir_cronograma_regressivo(
        parcelas_restantes - 1,
        valor_parcela
    )


print("\n=== CRONOGRAMA DE PARCELAMENTO ===")

parcelas = int(input("Digite a quantidade de parcelas: "))
valor_parcela = float(input("Digite o valor de cada parcela: R$ "))

exibir_cronograma_regressivo(parcelas, valor_parcela)