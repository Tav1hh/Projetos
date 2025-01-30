# Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro Valor é maior
# O Segundo Valor é maior
# Não existe valor maior, os dois são iguais
try:
    print("\033[33m=\033[m"*20)
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    print("\033[33m=\033[m"*20)

    if n1 > n2 :
        print("O \033[33mPrimeiro\033[m Valor é \033[34mMaior!\033[m")
    elif n2 > n1:
        print("O \033[33mSegundo\033[m Valor é \033[34mMaior!\033[m")
    elif n1 == n2:
        print("\033[33mNão Existe \033[mValor Maior, Os Dois são \033[34mIguais!\033[m")
except:
    print("\033[31mDigite um número válido\033[m")
