# Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# Equilatero: Todos os lados iguais
# Isosceles: Dois Lados Iguais
# Escaleno: Todos os lados diferentes
print("\033[33m=\033[m"*20)
print("Analisador de Retas")
print("\033[33m=\033[m"*20)
reta1 = int(input("Reta 1:"))
reta2 = int(input("Reta 2:"))
reta3 = int(input("Reta 3:"))
print("\033[33m=\033[m"*20)

retas = [reta1,reta2,reta3]
retas.sort()

if retas[0] + retas[1] >= retas[2]:
    print("É possivel criar um triangulo com essas retas")
    if retas[0] == retas[1] == retas[2]:
        print("Triangulo \033[32mEquilatero\033[m")
    elif retas[0] == retas[1] or retas[0] == retas[2] or retas[2] == retas[1]:
        print("Triangulo \033[32mIsósceles\033[m")
    elif retas[0] != retas[1] != retas[2]:
        print("Triangulo \033[32mEscaleno\033[m")
else:
    print("Não é possivel criar um triangulo com essas retas")