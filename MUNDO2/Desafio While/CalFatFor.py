num = int(input('Digite um numero pra calcular o fatorial:'))
fat = 1
print(f'Calculando o {num}!:')
for i in range(num,0,-1):
    fat *= i
    print(i,end='')
    print(' x ' if i > 1 else ' = ', end='')
print(fat)