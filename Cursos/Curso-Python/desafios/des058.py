# Melhore o jogo do desafio 028, onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.abs
from random import randint
computador = randint(0,10)
pessoa = input("Seu Palpite de 0-10: ")
cont = 1
while pessoa.isnumeric() == False:
    pessoa = input("\033[31mPalpite Inválido\033[m, escolha de 0-10: ")
while int(pessoa) != computador:
    print("\033[31mErrou!\033[m, Pensei em {}".format(computador))
    computador = randint(0,10)
    pessoa = input("Novo Palpite de 0-10: ")
    while pessoa.isnumeric() == False:
        pessoa = input("\033[31mPalpite Inválido\033[m, escolha de 0-10: ")
    cont = cont + 1
print("\033[32mAcertou!\033[m, você fez {} palpites".format(cont))