# O computador escolhe um número de 0 a 5 e o úsuario tenta descobrir
from random import randint
from time import sleep
computador = randint(0,5)
print("-=-"*20)
print("Vou pensar em um número entre 0 e 5, tente adivinhar..")
print("-=-"*20)
jogador = int(input("Qual eu pensei?: "))
print("PROCESSANDO...")
sleep(3)
# Verifica se o jogador ganhou
if jogador == computador:
    print("Parabens!! você acertou eu pensei em:",computador)
else:
    print("Não foi dessa vez.., eu pensei em:",computador)
print("Fim do jogo!")