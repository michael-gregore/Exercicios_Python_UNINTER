# Exercício 1 de 4 da atividade prática

# Texto de boas-vindas.
print('Bem-vindo a Loja do Michael Gregore Santos Ventura')

# Entradas feitas pelo usuário.
valor_unidade = float(input('Favor informar valor do produto: '))
valor_quantidade = int(input('Favor informar a quantidade do produto: '))

# Cálculo de multiplicação. Compra total sem desconto.
valor_mult = valor_unidade * valor_quantidade

# Condições e cálculos.
if valor_quantidade < 200:                                                  # Quantidade menor que 200 unidade.
    print('O valor SEM desconto: R$ {:.2f} reais'.format(valor_mult))       # Exibe na tela o valor sem desconto.

elif 200 <= valor_quantidade < 1000:                                        # Quantidade entre 200 e 999 unidades.
    calc_desconto = valor_mult - (0.05 * valor_mult)                        # Cálculo para saber a porcentagem (5%).
    print('O valor SEM desconto: R$ {:.2f} reais'.format(valor_mult))       # Exibe na tela o valor sem desconto.
    print('O valor COM desconto: R$ {:.2f} reais'.format(calc_desconto))    # Exibe na tela o valor com desconto.

elif 1000 <= valor_quantidade < 2000:                                       # Quantidade entre 1000 e 1999 unidades.
    calc_desconto = valor_mult - (0.10 * valor_mult)                        # Cálculo para saber a porcentagem (10%).
    print('O valor SEM desconto: R$ {:.2f} reais'.format(valor_mult))       # Exibe na tela o valor sem desconto.
    print('O valor COM desconto: R$ {:.2f} reais'.format(calc_desconto))    # Exibe na tela o valor com desconto.

else:                                                                       # Última condição sendo igual ou mais de 2000 unidades.
    calc_desconto = valor_mult - (0.15 * valor_mult)                        # Cálculo para saber a porcentagem (15%).
    print('O valor SEM desconto: R$ {:.2f} reais'.format(valor_mult))       # Exibe na tela o valor sem desconto.
    print('O valor COM desconto: R$ {:.2f} reais'.format(calc_desconto))    # Exibe na tela o valor com desconto.
