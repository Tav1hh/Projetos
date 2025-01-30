# Lé uma frase e mostra quantas letras 'a' tem, em que posição aparece a primeira, em que posição aparece pela ultima vez
frase = str(input("Frase: ")).strip().upper()
print("Quantos 'A':", frase.count('A'))
print("Primeiro 'A':", frase.find('A') + 1)
print("Ultimo 'A':", frase.rfind('A') + 1)