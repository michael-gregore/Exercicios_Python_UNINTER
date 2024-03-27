
soma = 0 # 2 + 4 = 6
cont = 0 # 1, 2

for i in range(1, 6, 1):
    if i % 2 == 0:
        soma += i
        cont += 1
media = soma / cont # 6 / 2

print('A media dos números pares é: {}'.format(media))
