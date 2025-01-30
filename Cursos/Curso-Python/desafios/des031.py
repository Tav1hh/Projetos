# Calcula o valor da viagem, até 200KM cobra 0,50, mais que isso, cobra 0,45
km = int(input("Quantos Kms?: "))
if km > 200:
    valor = 0.45 * km
else:
    valor = 0.5 * km
print("O valor da viagem ficou em R${:.2f}".format(valor))