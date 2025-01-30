# Mostra o nome em maiusculas, minusculas, quantas letras tem sem considerar os espaços, quantas letras tem o primeiro nome
nome = str(input("Nome completo: ")).strip()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
print(len(nome.split()[0]))