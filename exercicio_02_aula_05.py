
def valida_int(pergunta, minimo, maximo):
    entrada = int(input(pergunta))
    while (entrada < minimo) or (entrada > maximo):
        entrada = int(input(pergunta))
    return entrada

def soma_intervalo(inicio, fim):
    soma = 0
    i = inicio
    while i <= fim:
        soma += i
        i = i + 1
    return soma

x = valida_int('Digite um valor inteiro e positivo: ', 1, 99999)
y = valida_int('Digite um segundo valor inteiro e positivo: ', 1, 99999)

print('Somatório entre {} e {} é {}'.format(x, y, soma_intervalo(x, y)))
