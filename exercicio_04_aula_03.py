

salario = float(input('Informe o seu salário atual:'))
tempo = int(input('Informe o tempo de serviço na empresa:'))

if tempo > 10:
    bonus = salario * 0.3
else:
    if tempo > 5:
        bonus = salario * 0.2
    else:
        bonus = salario * 0.1

print('A sua bonificação é de {}'.format(bonus))
print('Seu salario final é {}'.format(salario + bonus))
