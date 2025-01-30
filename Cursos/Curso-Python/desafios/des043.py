# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5, Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
print("\033[33m=\033[m"*20)
print("\033[34mCalculadora de IMC\033[m")
print("\033[33m=\033[m"*20)
altura = float(input("Digite sua altura em M²: "))
peso = float(input("Digite seu Peso em Kg: "))
print("\033[33m=\033[m"*20)

imc = peso/altura**2

if imc < 18.5:
    print("\033[31mAbaixo do Peso\033[m")
elif imc < 25:
    print("\033[32mPeso Ideal\033[m")
elif imc < 30:
    print("\033[33mSobrepeso\033[m")
else:
    print("\033[31mObesidade Mórbida\033[m")