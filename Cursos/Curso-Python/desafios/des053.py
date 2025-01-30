# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
palavra = ''.join(str(input("Digite uma frase: ")).split())
inverso = palavra[::-1]
if palavra == inverso:
    print("É um Palindromo!")
else:
    print("Não é um Palindromo!")