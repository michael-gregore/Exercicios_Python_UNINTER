# Exercício 2 de 4 da atividade prática

# Menssagem de boas-vindas
print('Bem-vindo a Sorveteria do Michael Gregore Santos Ventura')

# Menu do programa
print('-' * 40 + 'Cardápio' + '-' * 36)
print('| Nº DE BOLAS  | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1       |      R$ 6,00           |      R$ 7,00       |      R$ 8,00        |')
print('|      2       |      R$ 10,00          |      R$ 12,00      |      R$ 14,00       |')
print('|      3       |      R$ 14,00          |      R$ 17,00      |      R$ 20,00       |')
print('-' * 84)

soma = 0    # Variavel que recebe os valores dos sorvetes e soma a si mesma

# Começo do laço
while True:

    sabor = input('\nInforme o sabor desejado (tr/pr/es): ')                                # Primeira entrada do usuario informando qual sabor
    if sabor == 'tr' or sabor == 'pr' or sabor == 'es':                                     # Condição para verificar o sabor escolhido
        quantidade = input('Informe a quantidade de bolas de sorvete desejado (1/2/3): ')   # Segunda entrada do usuario informando a quantidade de bolas de sorvete
    else:                                                                                   # Condição caso o usuario entre com escolha errada
        print('Sabor inválido. Tente novamente. ')
        continue                                                                            # Caso condição sabor errado, o programa vai reiniciar do começo do laço

    if quantidade == '1' or quantidade == '2' or quantidade == '3':                         # Condição para verificar a quantidade escolhida de bolas de sorvete

        if sabor == 'tr' and quantidade == '1':                                             # Se condição aceita, a variavel valor recebe 6.00 e a variavel soma recebe ela mesma mais o valor
            valor = 6.00
            soma += valor
            print('O seu pedido foi {} bola de sorvete TRADICIONAL: R$ 6,00 reais'.format(quantidade))      # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        elif sabor == 'tr' and quantidade == '2':                                           # Se condição aceita, a variavel valor recebe 10.00 e a variavel soma recebe ela mesma mais o valor
            valor = 10.00
            soma += valor
            print('O seu pedido foi {} bolas de sorvete TRADICIONAL: R$ 10,00 reais'.format(quantidade))    # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        elif sabor == 'tr' and quantidade == '3':                                           # Se condição aceita, a variavel valor recebe 14.00 e a variavel soma recebe ela mesma mais o valor
            valor = 14.00
            soma += valor
            print('O seu pedido foi {} bolas de sorvete TRADICIONAL: R$ 14,00 reais'.format(quantidade))    # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        elif sabor == 'pr' and quantidade == '1':                                           # Se condição aceita, a variavel valor recebe 7.00 e a variavel soma recebe ela mesma mais o valor
            valor = 7.00
            soma += valor
            print('O seu pedido foi {} bola de sorvete PREMIUM: R$ 7,00 reais'.format(quantidade))          # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        elif sabor == 'pr' and quantidade == '2':                                           # Se condição aceita, a variavel valor recebe 12.00 e a variavel soma recebe ela mesma mais o valor
            valor = 12.00
            soma += valor
            print('O seu pedido foi {} bolas de sorvete PREMIUM: R$ 12,00 reais'.format(quantidade))        # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        elif sabor == 'pr' and quantidade == '3':                                           # Se condição aceita, a variavel valor recebe 17.00 e a variavel soma recebe ela mesma mais o valor
            valor = 17.00
            soma += valor
            print('O seu pedido foi {} bolas de sorvete PREMIUM: R$ 17,00 reais'.format(quantidade))        # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        elif sabor == 'es' and quantidade == '1':                                           # Se condição aceita, a variavel valor recebe 8.00 e a variavel soma recebe ela mesma mais o valor
            valor = 8.00
            soma += valor
            print('O seu pedido foi {} bola de sorvete ESPECIAL: R$ 8,00 reais'.format(quantidade))         # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        elif sabor == 'es' and quantidade == '2':                                           # Se condição aceita, a variavel valor recebe 14.00 e a variavel soma recebe ela mesma mais o valor
            valor = 14.00
            soma += valor
            print('O seu pedido foi {} bolas de sorvete ESPECIAL: R$ 14,00 reais'.format(quantidade))       # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        elif sabor == 'es' and quantidade == '3':                                           # Se condição aceita, a variavel valor recebe20.00 e a variavel soma recebe ela mesma mais o valor
            valor = 20.00
            soma += valor
            print('O seu pedido foi {} bolas de sorvete ESPECIAL: R$ 20,00 reais'.format(quantidade))       # Informa ao usuario a quatidade de bolas de sorvete, sabor e o valor escolhido

        saida = input('Para um novo pedido digite (s). Para sair digite qualquer outra tecla: ')            # Terceira entrada do usuário perguntando se o mesmo quer continuar pedindo ou sair

    else:                                                                                # Caso condição de escolha errada da quatidade, informar em tela ao usuário e voltar ao inicio do laço
        print('Quantidade de bolas de sorvete inválido. Tente novamente. ')
        continue

    if saida == 's':                                                                        # Se condição verdade, continua efetuando os pedidos
        continue
    else:
        print('\nValor total do pedido a ser pago: R$ {:.2f} reais'.format(soma))           # Se condição falsa, encerra o programa
        break
