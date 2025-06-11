#Existem 2 metodos para import: o (import bebidas = vai colocar todas as bebidas do catalogo.) e a (FROM bebidas import = que permite escolher alguma
#bebida do catalogo).

"""import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é {math.ceil(raiz)}."""

'''from math import sqrt, floor

num = int(input('Digite um numero para saber a raiz quadrada: '))
raiz = sqrt(num)

print('Raiz quadrada de {} é: {:.2f}'.format(num, floor(raiz)))'''


'''from math import sqrt, floor

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {floor(raiz):.2f}.')'''


import emoji

print(emoji.emojize('Ola mundo :medalha_de_ouro:', language='pt'))

