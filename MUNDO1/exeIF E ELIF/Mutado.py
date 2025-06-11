import time

vel = int(input('Digite sua velocidade: '))
mut = (vel-80)*7

print('Vamos analisar sua velocidade.')
time.sleep(2.2)

if vel > 80:
    print('VOCE FOI MULTADO por dirigir acima da velocidade permitida.')
    print(f'Voce vai ter que pagar R$ {mut:.2f}.')
else:
    print('Muito bem, dirija com cuidado. ')
