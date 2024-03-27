
inicial = int(input('Digite um número: '))

print('Tabuada do número {}'.format(inicial))

x = inicial
y = 1

while y <= 10:
    calc = x * y
    print('{} x {} = {}'.format(y, x, calc))
    y += 1
