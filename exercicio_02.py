dias = int(input('Quantos dias?:'))
horas = int(input('Quantas horas?:'))
minutos = int(input('Quantos minutos?:'))
segundos = int(input('Quantos Segundos?:'))

soma = segundos+ (minutos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

s1 = ('Essa é a quantidade total em segundos: {}'.format(soma))

print(s1)