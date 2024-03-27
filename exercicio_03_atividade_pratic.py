# Exercício 3 de 4 da atividade prática

print('Bem-vindo ao PetShop do Michael Gregore Santos Ventura') # Exibe menssagem de boas_vindas


def cachorro_peso(pergunta_peso):                               # Primeira função que trata as entradas de peso
    base = 0                                                    # guarda o valor base de acordo com o peso escolhido
    while True:
        try:                                                    # Ele taz uma tentativa do código
            entrada = float(input(pergunta_peso))
            if entrada >= 50:
                print('Não aceitamos cachorros com esse peso! Digite o peso novamente.')
                continue
            elif entrada < 3:
                base = 40
                break
            elif (entrada >= 3) and (entrada <= 10):
                base = 50
                break
            elif (entrada >= 10) and (entrada <= 30):
                base = 60
                break
            elif (entrada >= 30) and (entrada < 50):
                base = 70
                break
        except ValueError:                                      # Caso o usuario digite qualquer caracter que não seja um número
            print('Entrada invalida! Digite o peso novamente.')
    return base                                                 # retorna o valor da base para o nome da função


def cachorro_pelo(pergunta_pelo):                           # Segunda função que trata as entradas de tipos de pelos
    multiplicador = 0                                       # guarda o valor do multiplicador de acordo com o pelo escolhido

    while True:
        entrada = input(pergunta_pelo)
        entrada = entrada.lower()                           # Caso o usuario tente digitar letras maiúsculas

        if entrada == 'c':
            multiplicador = 1
            break
        elif entrada == 'm':
            multiplicador = 1.5
            break
        elif entrada == 'l':
            multiplicador = 2
            break
        else:
            print('Opção invalida! Iforme novamente a opção.')
            continue
    return multiplicador                                   # retorna o valor do multiplicador para o nome da função


def cachorro_extra(pergunta_adicional):                     # Terceira função que trata as entradas de opcionais
    extra = 0                                               # guarda o valor extra de acordo com o opcional escolhido
    while True:
        try:
            entrada = int(input(pergunta_adicional))
            if entrada == 1:
                extra += 10
            elif entrada == 2:
                extra += 12
            elif entrada == 3:
                extra += 15
            elif entrada == 0:
                break
            else:
                print('Opção Invalida ! Informe opção novamente.')
                continue
        except ValueError:                                          # Caso o usuario digite qualquer caracter que não seja um número
            print('Opção Invalida ! Informe opção novamente.')
    return extra                                                    # retorna o valor de extra para o nome da função


a = cachorro_peso('\nInforme o peso do cachorro: ')                 # Chama a função que trata do peso
b = cachorro_pelo('\nQual tipo de pelo do cachorro'                 # Chama a função que trata do tipo de pelo
                  '\nc - Pelo Curto'
                  '\nm - Pelo Médio'
                  '\nl - Pelo Longo'
                  '\nInforme a opcão (c / m / l): ')
c = cachorro_extra('\nDeseja adicionar mais algum serviço?'         # Chama a função que trata dos opcionais
                   '\n1 - Corte de Unhas - R$ 10,00'
                   '\n2 - Escovar os Dentes - R$ 12,00'
                   '\n3 - Limpeza de Orelhas - R$ 15,00 '
                   '\n0 - Encerrar'
                   '\nInforme a opcão (1 / 2 / 3 / 0): ')

total = (a * b) + c                                                 # Calculo total das entradas

print('\nTotal a pagar(R$): {:.2f} (peso: {} * pelo: {} + adicional(is): {})'.format(total, a, b, c))   # Exibe menssagem final
