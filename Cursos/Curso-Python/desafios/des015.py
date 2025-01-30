# Calcula o aluguel de carros
dias = int(input("Quantos dias alugados? "))
kms = int(input("Quantos Km rodados? "))
valor = (dias*60) + (kms*0.15)
print("O total a pagar é de R${:.2f}".format(valor))