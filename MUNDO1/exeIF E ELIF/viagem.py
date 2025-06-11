vi = int(input('Digite a kilometragem da sua viagem: '))

v1 = vi * 0.50
v2 = vi * 0.45

if vi > 200:
    print(f'Sua viagem vai custar R$ {v2:.2f}.')
else:
    print(f'Sua viagem vai custar R$ {v1:.2f}.')