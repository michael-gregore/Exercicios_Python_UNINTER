consumo = float(input('Informe o consumo em Kwh: '))

print('\n(R) Residência''\n(I) Indústria''\n(C) Comércio')

tipo = input('\nConforme menu acima, informe o tipo da instalação: ')

if tipo == 'r' and consumo < 501:
    calc = consumo * 0.40
    print('\nValor total a pagar é de R$ {} reais'.format(calc))
elif tipo == 'r' and consumo > 500:
    calc = consumo * 0.65
    print('\nValor total a pagar é de R$ {} reais'.format(calc))

elif tipo == 'i' and consumo < 5001:
    calc = consumo * 0.55
    print('\nValor total a pagar é de R$ {} reais'.format(calc))
elif tipo == 'i' and consumo > 5000:
    calc = consumo * 0.60
    print('\nValor total a pagar é de R$ {} reais'.format(calc))

elif tipo == 'c' and consumo < 1001:
    calc = consumo * 0.55
    print('\nValor total a pagar é de R$ {} reais'.format(calc))
elif tipo == 'c' and consumo > 1000:
    calc = consumo * 0.60
    print('\nValor total a pagar é de R$ {} reais'.format(calc))

else:
    print('\nOperação Invalida!')