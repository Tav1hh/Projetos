# Le a largura e altura e mostra a quantidade de tinta para pinta-la
altura = int(input("Altura:"))
largura = int(input("Largura:"))
area = altura*largura
tinta = area/2
print("Para pintar {}m² vai ser preciso {}l de tinta".format(area,tinta))
