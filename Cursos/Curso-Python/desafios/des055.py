# Faça um programa que leia o peso de 5 pessoas, no final mostre qual foi o maior e o menor peso lidos.
for c in range(1,6):
    peso = float(input("Peso {}: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print("Maior Peso: {}Kg, Menor Peso {}Kg".format(maior,menor))