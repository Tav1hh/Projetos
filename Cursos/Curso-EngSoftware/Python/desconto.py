un = eval(input('Unidades:  '))
total = un*10

if un >20:
    desc = (total*20)/100

elif un >10:
    desc = (total*10)/100

else:
    print('Sem desconto')
    desc = 0

print(f'Valor final {total} com desconto de {desc}, fica {total-desc}')