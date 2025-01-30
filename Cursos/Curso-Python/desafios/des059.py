# Crie um programa que leia dois valores e mostre um menu na tela:
# 1 - Somar
# 2 - Multiplicar
# 3 - Maior
# 4 - Novos números
# 5 - Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
opt = 0
while opt != 5:
    n1 = input("1º número: ")
    while n1.isnumeric() == False:
        n1 = input("\033[31mERRO\033[m, Digite um número válido: ")
    n2 = input("2º número: ")
    while n2.isnumeric() == False:
        n2 = input("\033[31mERRO\033[m, Digite um número válido: ")
    n1 = int(n1)
    n2 = int(n2)
    print("\033[33m=\033[m"*20)
    # Lista de opções
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do Programa")
    opt = input("\033[34mOpção\033[m: ")
    while opt not in '12345':
        print("ERRO, escolha uma opção válida!")
        opt = input("\033[34mOpção\033[m: ")
    opt = int(opt)
    print("\033[33m=\033[m"*20)
    # Operações
    if opt == 1:
        print("A Soma entre {} e {} = {}".format(n1,n2,n1+n2))
        print("\033[33m=\033[m"*20)

    elif opt == 2:
        print("A Multiplicação entre {} e {} = {}".format(n1,n2,n1*n2))
        print("\033[33m=\033[m"*20)

    elif opt == 3:
        maior = n1
        if n1 < n2:
            maior = n2
        print("O Maior número é {}".format(maior))
        print("\033[33m=\033[m"*20)

    elif opt == 4:
        print("Digite os novos números..")
print("\033[32mPrograma finalizado!\033[m")

