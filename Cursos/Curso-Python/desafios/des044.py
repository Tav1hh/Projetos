# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# A Vista Dinheiro/Cheque: 10% de desconto
# A Vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input("Valor do produto: "))
print("\033[33m=\033[m"*20)
print("Forma de Pagamento:")
print("1 - Dinheiro/Cheque")
print("2 - 1x Cartão")
print("3 - 2x Cartão")
print("4 - 3x ou mais no Cartão")
opt = int(input("Opção: "))
print("\033[33m=\033[m"*20)

if opt == 1:
    desc = 10 * 100 / valor
    novoValor = valor - desc
    print("Valor do produto de R${} por R${} Desconto de 10%".format(valor,novoValor))
elif opt == 2:
    desc = 5 * 100 / valor
    novoValor = valor - desc
    print("Valor do produto de R${} por R${} Desconto de 5%".format(valor,novoValor))
elif opt == 3:
    print("Valor do produto de R${} por R${} Valor normal".format(valor,valor))
elif opt == 4:
    juros = 20 * 100 / valor
    novoValor = valor + juros
    print("Valor do produto de R${} por R${} juros de 20%".format(valor,novoValor))