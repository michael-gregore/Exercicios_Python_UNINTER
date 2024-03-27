
a = 1
b = 2
c = 3
x = 20
y = 10
z = -1

v1 = 'v' == 'v'     # Verdadeiro
v2 = 'v' == 'f'     # Falso

nome = 'pedro'
rua = 'pedrinho'

letra_a = a + (c / b)
print('Respota da letra a): {}'.format(letra_a))

letra_b = c / b / a
print('Resposta da letra b): {}'.format(letra_b))

letra_c = -x ** b
print('Resposta da letra c): {}'.format(letra_c))

letra_d = (-x) ** b
print('Resposta da letra d): {}'.format(letra_d))

letra_e = v1 or v2
print('Resposta da letra e): {}'.format(letra_e))

letra_f = v1 and not v2
print('Resposta da letra f): {}'.format(letra_f))

letra_g = v2 and not v1
print('Resposta da letra g): {}'.format(letra_g))

letra_h = not nome == rua
print('Resposta da letra h): {}'.format(letra_h))

letra_i = v1 and not v2 or v2 and not True
print('Resposta da letra i): {}'.format(letra_i))

letra_j = x > y and c <= b
print('Resposta da letra j): {}'.format(letra_j))

letra_k = c - 3 * a < x + 2 * z
print('Resposta da letra k): {}'.format(letra_k))
