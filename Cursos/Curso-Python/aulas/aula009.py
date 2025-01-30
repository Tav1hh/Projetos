# Manipulando cadeias de caracteres
frase = "Curso em Video Python"
print(frase[9:14:1]) # Fatiamento
# Análise:
print(len(frase)) # Retorna o Cumprimento da String
print(frase.find("Video")) # Retorna o indice em que começa essa frase/palavra/caractere
print(frase.count('o',0,5)) # Conta quantas vezes esse caractere aparece
print("Curso" in frase) # Retorna um valor booleano para caso exista essa palavra na string
#Transformação
print(frase.replace("Python", "Android")) #Substitui uma palavra pela outra
print(frase.upper()) # Passa tudo para maiusculas
print(frase.lower()) # Passa tudo para minusculas
print(frase.capitalize()) # Passa todas as primeiras letras de cada palavra para maiusculas
print(frase.title()) # Coloca somente a primeira letra em maiusculas
print(frase.strip()) # Tira todos os espaços antes e apos a frase
print(frase.split()) # Retorna uma lista com cada palavra da string
print("-".join(frase)) # Monta uma frase apartir de uma lista usando como jução o caractere escolhido




