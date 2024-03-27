p = float(input('Qual o preço do produto?:'))
d = int(input('Quantos % de desconto será aplicado ao produto?:'))

desconto = p * (d / 100)
valor_final = p - desconto

print('O desconto aplicado é de R${}, sendo assim o valor final do produto é de R${}'.format(desconto, valor_final))

