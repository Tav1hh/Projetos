# Crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for c in range(1,7):
    anoNascimento = int(input("Ano Nascimento da {}º Pessoa: ".format(c)))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print("Das 6 Pessoas, {} são responsaveis e {} não são".format(maior,menor))
