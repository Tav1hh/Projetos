# Lé o nome de uma cidade e diz se começa ou não com SANTO
cidade = str(input("Cidade: ")).upper().split()
print("Começa com Santo?:","SANTO" in cidade[0])