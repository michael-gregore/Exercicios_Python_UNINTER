
inicial = int(input('Digite o 1º número: '))
final = int(input('Digite o 2º número: '))

qtd_positivo = 0
qtd_par = 0
qtd_impar = 0
soma_positivo = 0
soma_par = 0
soma_impar = 0
cont = inicial

if inicial < final:
    while cont <= final:
        if cont > 0:
            qtd_positivo += 1
            soma_positivo += cont
        if cont % 2 == 0:
            qtd_par += 1
            soma_par += cont
        else:
            qtd_impar += 1
            soma_impar += cont
        cont += 1
    media_positivo = soma_positivo / qtd_positivo
    media_par = soma_par / qtd_par
    media_impar = soma_impar / qtd_impar

    print('Quantidade de valores positivos: {}'.format(qtd_positivo))
    print('Média de valores positivos: {}'.format(media_positivo))
    print('Quantidade de valores pares: {}'.format(qtd_par))
    print('Média de valores pares: {}'.format(media_par))
    print('Quantidade de valores impares: {}'.format(qtd_impar))
    print('Média de valores impares: {}'.format(media_impar))

else:
    print('Você digitou um valor inicial maior ou igual ao final. Encerrando o programa...')
