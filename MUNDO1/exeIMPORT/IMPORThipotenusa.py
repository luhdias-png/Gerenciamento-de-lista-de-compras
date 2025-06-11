import math

ca = float(input('Comprimento do Cateto Oposto: '))
caad = float(input('Comprimento do Cateto Adjacente: '))

hi= math.hypot(ca, caad)

print(f'A hipotenusa é {hi:.2f}.')