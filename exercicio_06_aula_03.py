nota_1 = float(input('Digite a nota final de Português:'))
nota_2 = float(input('Digite a nota final de Matemática:'))
nota_3 = float(input('Digite a nota final de Ciências:'))

if nota_1 >= 7 and nota_2 >= 7 and nota_3 >= 7:
    print('\nParabéns !!! Você passou de ano.')
else:
    print('\nQue pena... Você não passou de ano.')
