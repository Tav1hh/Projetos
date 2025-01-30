# Desenvolva um programa que leia o primeiro termo e a razão de uma PA, no final, mostres os 10 primeiros termos dessa progressão.abs
inicio = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a Razão do PA: "))

for c in range(0,10):
    print(inicio+razao*c,end=",")