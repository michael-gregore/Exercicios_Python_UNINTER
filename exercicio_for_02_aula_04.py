
x = int(input('A tabuada será de qual número: '))
y = int(input('Digite um número final: '))

for i in range(1, y+1, 1):

    print('{} x {} = {}'.format(x, i, x*i))
