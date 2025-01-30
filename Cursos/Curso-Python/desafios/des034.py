# Aplica um aumento de 10% para salarios acima de 1250 e aumento de 10% para salarios abaixo.
salario = float(input("Salario: "))
if salario > 1250:
    aumento = 10
    salario = salario + salario * aumento / 100
else:
    aumento = 15
    salario = salario + salario * aumento / 100
print("Aumento de {}%, novo sálario R${:.2f}".format(aumento,salario))