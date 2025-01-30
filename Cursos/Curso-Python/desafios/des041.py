# A Confedereção Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
# até 9 anos: Mirim
# até 14 anos: Infantil
# até 19 anos: Junior
# até 20 anos: Senior
# Acima: Master
from datetime import date
anoNascimento = int(input("Ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 20:
    print("Senior")
else:
    print("Master")