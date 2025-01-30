# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura While.abs
inicio = int(input("Inicio: "))
razao = int(input("Razão da PA: "))
ini = inicio
while ini < (razao*10+inicio):
    print(ini,end=",")
    ini = ini + razao

