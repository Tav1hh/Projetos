# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

dia = int(input("Dia Nascimento: "))
mes = int(input("Mes Nascimento: "))
ano = int(input("Ano Nascimento: "))

dataNascimento = date(ano,mes,dia)
dataAtual = date.today()
dataAlistar = dataNascimento.replace(year=dataNascimento.year+18)

if dataAtual.year - dataNascimento.year < 18:
    print("Ainda não chegou o momento de se alistar \033[33mfaltam {} dias\033[m".format((dataAlistar - dataAtual).days))
# Chegou a hora de se alistar
elif dataAtual.year - dataNascimento.year == 18:
    print("Esse Ano você completa 18 anos, se \033[33mALISTE\033[m")
# Passou do momento de se alistar
elif dataAtual.year - dataNascimento.year > 18:
    print("Seu alistamento \033[31mPassou..\033[m ha {} dias".format((dataAtual - dataAlistar).days))   


