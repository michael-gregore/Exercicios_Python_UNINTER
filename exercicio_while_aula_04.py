
entrada_01 = int(input('Digite o 1º número: '))
entrada_02 = int(input('Digite o 2º número: '))

soma = 0        # Variavel 'soma' começando sempre com zero
contador = 1    # Variavel 'contador' começando pelo um

while contador <= entrada_01:   # Condição para permanecer no loop
    soma += entrada_02          # Variavel somando ela mesma com a segunda entrada do usuario
    contador += 1               # Variavel contador
print('Resultado da multiplicação: {} x {} = {}'.format(entrada_01, entrada_02, soma))
