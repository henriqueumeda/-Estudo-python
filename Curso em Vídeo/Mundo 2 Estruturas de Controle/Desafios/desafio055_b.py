lista = []

for contador in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(contador)))
    lista += [peso]

print('O maior peso da lista foi {}Kg'.format(max(lista)))
print('O menor peso da lista foi {}Kg'.format(min(lista)))