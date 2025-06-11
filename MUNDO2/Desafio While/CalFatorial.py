num = int(input('Digite um numero para saber seu fatorial:'))
fat = num
mul = 1
print(f'Calculando {num}! = ')
while fat > 0:
    print(f'{fat}', end='')
    print(f' x 'if fat > 1 else ' = ',end='')
    mul *= fat
    fat -= 1
print(mul)