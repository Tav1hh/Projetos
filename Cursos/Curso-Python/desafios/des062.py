# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos, O programa encerra quando ele disser que quer ver 0 termos.
inicio = int(input("Inicio: "))
razao = int(input("Razão da PA: "))
print("\033[33m=\033[m"*20)
termos = 10
while termos != 0:
    ini = inicio
    while ini < (razao*termos+inicio):
        print("\033[34m{}\033[m".format(ini),end=",")
        ini = ini + razao
    print()
    print("\033[33m=\033[m"*20)
    termos = int(input("Quantos Termos você quer ver? [0] sair: "))
    print("\033[33m=\033[m"*20)
print("\033[32mPrograma encerrado!\033[m")
