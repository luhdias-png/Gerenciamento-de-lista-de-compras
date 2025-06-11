print('-='*20)
print(f'Analisador de triangulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('-='*20)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Eles PODEM fazer um triangulo.')
else:
    print('Eles NAO PODEM fazer um triangulo.')