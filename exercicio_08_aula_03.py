print('No menu a baixo escolha uma fruta:\n')
print('1 - Maçã\n''2 - Laranja\n''3 - Banana')

e = int(input('\nQual fruta você escolhe ?: '))
q = int(input('Quantas você quer comprar ?: '))

if e == 1:
    pagar = q * 2.3
    print('\nVocê comprou {} Maçãs. Total à pagar: R$ {}'.format(q, pagar))

elif e == 2:
    pagar = q * 3.6
    print('\nVocê comprou {} Laranjas. Total à pagar: R$ {}'.format(q, pagar))

elif e == 3:
    pagar = q * 1.85
    print('\nVocê comprou {} Bananas. Total à pagar: R$ {}'.format(q, pagar))

else:
    print('Produto Inexistente !!!')
