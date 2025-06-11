from random import randint
import time
print('-='*25)
print(f'{"JO KEN PO NERD":=^50}')
print('-='*25)

vs = ('tesoura', 'papel', 'pedra', 'lagarto', 'spock')
pc = randint(0,4)
pla = int(input('Digite:\n[0]TESOURA.\n[1]PAPEL.\n[2]PEDRA.\n[3]LAGARTO.\n[4]SPOCK.\n:'))
time.sleep(1)
print(f'Vamos ver quem ganha.')
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!')
time.sleep(1)
print('-='*25)
print(f'Voce escolheu: {vs[pla]}')
print('-='*25)
print(f'O Computador escolheu: {vs[pc]}.')
print('-='*25)

if pc == 0 and pla == 1 or pla == 3:
    print('Pc ganhou.')
elif pc == 1 and pla == 2 or pla == 4:
    print('PC ganhou.')
elif pc == 2 and pla == 0 or pla ==3:
    print('PC ganhou.')
elif pc == 3 and pla == 4 or pla == 1:
    print('PC ganhou.')
elif pc == 4 and pla == 0 or pla == 2:
    print('PC ganhou.')
elif pla == pc:
    print('EMPATOU')
else:
    print('PLAYER GANHOU.')

