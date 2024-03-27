valor_compra = float(input('Favor informar o valor da sua compra: R$ '))

print('\n1 - Pagamento à vista''\n2 - Pagamento em 3x''\n3 - Pagamento em 5x''\n4 - Pagamento em 10x')

tipo_pagamento = int(input('\nEscolha a opção do menu acima que deseja pagar: '))

if tipo_pagamento == 1:
    calculo_desconto = valor_compra - (0.05 * valor_compra)
    print('\nUm desconto de 5% será aplicado na sua compra. O valor final da compra é de R$ {} reais'.format(calculo_desconto))
elif tipo_pagamento == 2:
    calculo_parcela = valor_compra // 3
    print('\nSerão 3x parcelas de R$ {} reais. O valor final da compra é de R$ {} reais'.format(calculo_parcela, valor_compra))
elif tipo_pagamento == 3:
    calculo_parcela = (valor_compra // 5)
    calculo_acrescimo = calculo_parcela + (0.02 * calculo_parcela)
    calculo_final = calculo_acrescimo * 5
    print('\nUm acrescimo de 2% será aplicado. Valor da parcela R$ {} reais. Valor final R$ {} reais'.format(calculo_acrescimo, calculo_final))
elif tipo_pagamento == 4:
    calculo_parcela = (valor_compra // 10)
    calculo_acrescimo = calculo_parcela + ( 0.08 * calculo_parcela )
    calculo_final = calculo_acrescimo * 10
    print('\nUm acrescimo de 8% será aplicado. Valor da parcela R$ {} reais. Valor final R$ {} reais'.format(calculo_acrescimo, calculo_final))
else:
    print('\nOpção Inválida !!!')
