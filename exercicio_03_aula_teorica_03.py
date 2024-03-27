ano_nascimento = int(input('Informe o seu ano de nascimento:'))
ano_atual = int(input('Em que ano estamos ?:'))

idade = (ano_atual - ano_nascimento)

print('A sua idade é: {} anos'.format(idade))

if (idade >= 18):
    print('Você é maior de idade e já pode tirar carteira de motorista ! ')
else:
    print("Você é menor de idade e por isso não pode tirar carteira de motorista !")