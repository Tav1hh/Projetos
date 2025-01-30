print('='*10)
print('Olá, Mundo!')
print('='*10)

print('valor',12345)
print('valor = {}'.format(12345))
print(f'valor = {12345}')
print('='*10)

#caracteristicas das variaveis em Python
nome = 'exemplo de string em Python'
print(nome)
print('valor da variavel nome = {}'.format(nome))
print(f'valor da variavel nome = {nome}')
print('='*10)

#atribuição multipla
a, b = 1,2
print('Antes da troca')
print(f'O valor das variaveis a={a}, b={b}')
#primeira troca
temp = a
a = b
b = temp
print('Primeira troca')
print(f'O valor das variaveis a={a}, b={b}')
#Segunda troca
a, b = b, a
print('Segunda troca')
print(f'O valor das variáveis: a={a}, b={b}')
print('='*10)

#Operadores matématicos
x = 3
x += 2
print(f'X Somado com 2 ={x}')
x -= 2
print(f'X Subtraindo 2 ={x}')
x *= 2
print(f'X multiplicado por 2 ={x}')
x /= 2
print(f'X Dividido por 2={x}')
x %= 2
print(f'Resto da divisõa de X por 2 ={x}')
print('='*10)

#Trabalhando com Listas
lista = [101,202,303,404,505]
print(f'Lista[0] = {lista[0]}')
print(f'Lista[1] = {lista[1]}')
print(f'Lista[2] = {lista[2]}')
print(f'Lista[3] = {lista[3]}')
print(f'Lista[4] = {lista[4]}')
print(f'Lista completa: {lista}')

print('='*10)
#Trabalhando com Dicionatios
pessoas = {1111:['nome 01'], 2222:['nome 02'], 3333:['nome 03'], 4444:['nome 04']}
print(f'Primeira Pessoa = {pessoas[1111]}')
print(f'Quarta Pessoa = {pessoas[4444]}')

print('='*10)