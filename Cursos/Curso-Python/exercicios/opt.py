def opcoes():
    print("\033[31m="*20)
    print("\033[33m1 - Somar")
    print("\033[33m2 - Subtrair")
    print("\033[33m3 - Dividir")
    print("\033[33m4 - Multiplicar")
    print("\033[31m="*20)
    opt = int(input("\033[mOpção: "))
    return opt
def somar():
    print("Números Somados!")
def subtrair():
    print("Números Subtraidos!")
def dividir():
    print("Números Divididos!")
def multiplicar():
    print("Números Múltiplicados!")

# Sistema
while True:
    opt = opcoes()
    if opt == 1:
        somar()
    elif opt == 2:
        subtrair()
    elif opt == 3:
        dividir()
    elif opt == 4:
        multiplicar()
    else:
        print("OPÇÂO INVALIDA!")