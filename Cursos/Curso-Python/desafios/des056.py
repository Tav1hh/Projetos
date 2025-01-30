# Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas, no final do programa, mostre:
# A Média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.abs
media = 0
mulheresNovas = 0
for c in range(1,5):
    nome = str(input("Nome {}: ".format(c)))
    idade = int(input("Idade {}: ".format(c)))
    sexo = str(input("Sexo M ou F: ".format(c))).upper()
    print("\033[33m=\033[m"*30)
    # Media
    media = media + idade
    # Homem mais velho
    if c == 1:
        nomeMaisVelho = nome
        idadeVelho = idade
    elif idade > idadeVelho and sexo == 'M':
        nomeMaisVelho = nome
        idadeVelho = idade
    # Mulheres abaixo de 20
    if idade < 20 and sexo == 'F':
        mulheresNovas = mulheresNovas + 1

print("A Média de idade: {}".format(media/4))
print("Homem mais velho: {}".format(nomeMaisVelho))
print("Quantidade de mulheres abaixo de 20 anos: {}".format(mulheresNovas))
