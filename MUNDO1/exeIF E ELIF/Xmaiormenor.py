n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))

baixo = n1

if n2 < n1 and n2 < n3:
    baixo = n2
elif n3 < n1 and n3 < n2:
    baixo = n3
print(f'O menor valor é {baixo}')
alto = n1
if n2 > n1 and n2 > n3:
    alto = n2
elif n3 > n1 and n3 > n2:
    alto = n3
print(f'O maior numero é {alto}')