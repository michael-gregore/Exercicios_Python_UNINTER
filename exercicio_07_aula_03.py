# Conter um número inteiro entre -100 até 100.

x = int(input('Digite um número inteiro:'))

if 0 <= x <= 100 or -100 <= x <= -1:
    print('Critério atendido !')
else:
    print('Critério não atendido !')
