num = (int(input('Digite um numero')),
       int(input('Digite outro numero')),
       int(input('Digite mais um numero')),
       int(input('Digite o ultimo numero')))
#Da pra colocar um input dentro de uma variavel

print(f'O numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3)+1} posicao')
else:
    print('O numero 3 nao foi adicionado.')
print(f'Os valores pares sao:', end='')
for n in num:
    if n %2 ==0:
        print(n, end= '')
