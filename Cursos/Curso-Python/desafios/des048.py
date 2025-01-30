# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 e 500.abs
num = 0
for c in range(1,501,2):
    if c%3 == 0:
        num += c
print("A soma de todos os números impares multiplos de 3 entre 0 e 500 é {}".format(num))
