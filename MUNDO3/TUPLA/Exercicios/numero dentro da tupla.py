# JEITO ERRADO
'''
import random
num = (random.randint(1,10),random.randint(1,10),random.randint(1,10),
       random.randint(1,10),random.randint(1,10))


print(f'Esses numeros estao sendo gerados automaticamente:')
for n in num:
    print(n, end=' ')
n_maior = num[0]#indice 0
n_menor = num[0]
if n > n_maior:
    n_maior = n
elif n < n_menor:
    n_menor = n

print(f'O maior numero é {n_maior}')
print(f'O menor numero é {n_menor}')

'''
import random

num = (random.randint(1,10),random.randint(1,10),random.randint(1,10),
       random.randint(1,10),random.randint(1,10))
print('Esses numeros foram gerados automaticamente: ')
for n in num:
    print(n, end='-')
print(f'O maior numero é {max(num)}')
print(f'O menor numero é {min(num)}')