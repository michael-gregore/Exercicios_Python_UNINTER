x = int(input('Qual primeira medida ?: '))
y = int(input('Qual segunda medida ?: '))
z = int(input('Qual terceira medida ?: '))

if x > 0 and y > 0 and z > 0:
    if x + y > z and x + z > y and y + z > x:
        if x != y and x != z and y != z:
            print('\nTriângulo Escaleno !')
        else:
            if x == y and y == z:
                print('\nTriângulo Equilátero !')
            else:
                print('\nTriângulo Isósceles !')
    else:
        print('\nAo menos um dos valores indicados não serve para formar um triângulo.01')
else:
    print('\nAo menos um dos valores indicados não serve para formar um triângulo.02')
