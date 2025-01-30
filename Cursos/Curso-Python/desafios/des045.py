# Crie um programa que faça o computador jogar JokenPô com você
from random import choice

computador = [1,2,3]
computador = choice(computador)

print("\033[33m=\033[m"*20)
print("Jogo de Jokenpô")
print("\033[33m=\033[m"*20)
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
jogador = int(input("Escolha sua opção: "))
print("\033[33m=\033[m"*20)

# Empates
if jogador == 1 and computador == 1:
    print("Empate, Nos Dois Jogamos Pedra..")
if jogador == 2 and computador == 2:
    print("Empate, Nos Dois Jogamos Papel..")
if jogador == 3 and computador == 3:
    print("Empate, Nos Dois Jogamos Tesoura..")
# Computador Ganha
if jogador == 1 and computador == 2:
    print("Eu Ganhei, Papel ganha de Pedra")
if jogador == 2 and computador == 3:
    print("Eu Ganhei, Tesoura Ganha de Papel")
if jogador == 3 and computador == 1:
    print("Eu Ganhei, Pedra ganha de Tesoura")
# Jogador Ganha
if computador == 1 and jogador == 2:
    print("Você Ganhou, Papel ganha de Pedra")
if computador == 2 and jogador == 3:
    print("Você Ganhou, Tesoura Ganha de Papel")
if computador == 3 and jogador == 1:
    print("Você Ganhou, Pedra ganha de Tesoura")