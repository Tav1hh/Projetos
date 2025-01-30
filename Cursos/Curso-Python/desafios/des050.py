# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares, Se o valor digitado for impar, Desconsidere-o
soma = 0
for c in range(1,7):
    n = int(input("Número {}: ".format(c)))
    if n%2 == 0:
        soma = soma + n
print("A soma de todos os números pares é {}".format(soma))
