
while True:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    if nome != 'Michael':
        print('_01Usuario ou senha incorretos!')
        continue
    if senha == '1234':
        break
    print('_02Usuario ou senha incorretos!')

print('Acesso concedido!')
