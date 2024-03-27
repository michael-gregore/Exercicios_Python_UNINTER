km = int(input('Quantos KM percorridos?:'))
dias = int(input('Quantos dias de aluguel?:'))

d = 60.00 * dias   # Preço do carro por dia
k = 0.15 * km     # Preço do carro por kilometro
calculo_final = d + k

print('O valor total dos dias foi de R$ {}'.format(d))
print('O valor total dos kilometros foi de R$ {}'.format(k))
print('Total a pagar é de R$ {}'.format(calculo_final))