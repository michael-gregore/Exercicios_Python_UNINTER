# Exercício 4 de 4 da atividade prática
ficha = {}                                                      # Dicionario vazio
lista_colaboradores = []                                        # Lista vazia
id_global = 0
def cadastrar_colaborador(id):                                  # Função para cadastrar
    print('*' * 76)
    print('-' * 30, 'MENU CADASTRAR COLABORADOR', '-' * 30)
    global id_global
    ficha['id'] = id_global + 1                                 # Populando o dicionario na chave 'id' com a variavel id_global
    id_global += 1
    print(f'ID do Colaborador {ficha["id"]}')
    ficha['nome'] = str(input('Digite nome: '))                 # Populando o dicionario na chave 'nome'
    ficha['setor'] = str(input('Digite o setor: '))             # Populando o dicionario na chave 'setor'
    ficha['pagamento'] = float(input('Digite o pagamento (R$): '))   # Populando o dicionario na chave 'pagamento'
    lista_colaboradores.append(ficha.copy())                    # Adiciona os dicionarios criados dentro da lista_colaboradores
def consultar_colaborador():                                    # Função para consultar
    # Menu contendo todas as opções que o usuario pode acessar
    while True:
        print('*' * 76)
        print('-' * 30, 'MENU CONSULTAR COLABORADOR', '-' * 30)
        print('1 - Consultar Todos os Colaboradores\n'
              '2 - Consultar Colaborador por ID\n'
              '3 - Consultar Colaborador(es) por setor\n'
              '4 - Retornar Ao Menu Principal')
        resposta = input('Informe opção desejada [1/2/3/4]: ')
        if resposta != '1' and resposta != '2' and resposta != '3' and resposta != '4':     # Estrutura de escolhas do menu consultar
            print('Opção Inválida! Informe uma das opções (1/2/3/4).')
        elif resposta == '1':
            for ficha in lista_colaboradores:                               # Varre dentro da lista_colaboradores e a variavel ficha se torna dicionarios
                for c, v in ficha.items():                                  # Varre dentro dos dicionarios trazendo agora as chaves e valores
                    print('{}: {}'.format(c, v))
        elif resposta == '2':
            resposta_2 = int(input('Informe o ID do colaborador: '))
            for ficha in lista_colaboradores:                               # Varre dentro da lista_colaboradores e a variavel ficha se torna dicionarios
                if ficha['id'] == resposta_2:                               # Verifica se resposta_2 é igual ao que está na chave 'id'
                    for c, v in ficha.items():                              # Varre dentro dos dicionarios trazendo agora as chaves e valores
                        print(f'{c}: {v}')
        elif resposta == '3':
            resposta_3 = str(input('Informe o setor do(s) colaborador(es): '))
            for ficha in lista_colaboradores:                               # Varre dentro da lista_colaboradores e a variavel ficha se torna dicionarios
                if ficha['setor'] == resposta_3:                            # Verifica se resposta_3 é igual ao que está na chave 'setor'
                    for c, v in ficha.items():                              # Varre dentro dos dicionarios trazendo agora as chaves e valores
                        print(f'{c}: {v}')
        elif resposta == '4':
            break
def remover_colaborador():                                                  # Função para remover
    print('*' * 76)
    print('-' * 30, 'MENU REMOVER COLABORADOR', '-' * 30)
    resposta = int(input('Digite o ID do colaborador a ser removido: '))
    for ficha in lista_colaboradores:                                       # Varre dentro da lista_colaboradores e a variavel ficha se torna dicionarios
        if ficha['id'] == resposta:
            lista_colaboradores.remove(ficha)                               # Remove o dicionario caso o ID escolhido seja localizado dentro do dicionario

#---------------------------- PROGRAMA PRINCIPAL -----------------------------------
print('Bem-vindo ao Controle de Colaboradores do Michael Gregore Santos Ventura')
# Menu contendo todas as opções que o usuario pode acessar
while True:
    print('*' * 76)
    print('-' * 30, 'MENU PRINCIPAL', '-' * 30)
    print('1 - Cadastrar Colaborador\n'
          '2 - Consultar Colaborador(es)\n'
          '3 - Remover Colaborador\n'
          '4 - Sair')
    resposta = input('Informe opção desejada [1/2/3/4]: ')
    if resposta != '1' and resposta != '2' and resposta != '3' and resposta != '4':     # Estrutura de escolhas do menu principal
        print('Opção Inválida! Informe uma das opções (1/2/3/4).')
    elif resposta == '1':
        cadastrar_colaborador(id_global)    # Chama a função cadastro com parâmetro recebendo uma varivael global
    elif resposta == '2':
        consultar_colaborador()             # Chama a função que ira consultar todos os colaboradores cadastrados
    elif resposta == '3':
        remover_colaborador()               # Chama a função que ira remover qualquer colaborador escolhido
    elif resposta == '4':
        break
