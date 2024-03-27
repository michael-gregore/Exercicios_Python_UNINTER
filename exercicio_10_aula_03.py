numero_1 = float(input('Digite o 1º número: '))
numero_2 = float(input('Digite o 2º número: '))

print('\n1 - Adição (+)\n''2 - Subtração (-)\n''3 - Multiplicação (*)\n''4 - Divisão (/)\n')

operacao = int(input('\nAgora escolha no menu acima, qual operação deseja fazer: '))

if operacao == 1:
    calculo = numero_1 + numero_2
    print('\nO resultado da soma é {} !'.format(calculo))
elif operacao == 2:
    calculo = numero_1 - numero_2
    print('\nO resultado da subtração é {} !'.format(calculo))
elif operacao == 3:
    calculo = numero_1 * numero_2
    print('\nO resultado da multiplicação é {} !'.format(calculo))
elif operacao == 4:
    calculo = numero_1 / numero_2
    print('\nO resultado da divisão é {} !'.format(calculo))
else:
    print('\nOpção Invalida !')
