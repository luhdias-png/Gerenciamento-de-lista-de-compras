import os

while True:
    print('=-'*10)
    print('Tabuada')
    print('=-'*10)
    n = int(input('Digite um numero para ver a tabuada\n:'))
    os.system('cls')
    if n >0:
        for i in range(1,11):
            print(f'{i} x {n} = {i * n}')
    else:
        break
print('Obrigado por usar meu programa.')
            