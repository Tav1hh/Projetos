# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.abs
sexo = str(input("informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("\033[31mDado inválido!\033[m informe seu sexo [M/F]: ")).strip().upper()[0]
print("Sexo '{}' Registrado".format(sexo))