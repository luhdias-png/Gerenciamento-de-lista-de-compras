import random
import time
import emoji
#------------------------------------------------------------------------------------
print('-='*25)
print(f'{"JO KEN PO NERD":=^50}')
print('-='*25)

vs = ['tesoura', 'papel', 'pedra', 'lagarto', 'spock']
pc = random.choice(vs)
pla = int(input('Digite:\n[1]TESOURA.\n[2]PAPEL.\n[3]PEDRA.\n[4]LAGARTO.\n[5]SPOCK.\n:'))
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
print(f'Voce escolheu: {vs[pla -1 ]}')
print('-='*25)
print(f'O Computador escolheu {pc}.')
if pc == 'tesoura':
    if pla == 1:
        print('EMPATE')
    elif pla == 2:
        print('DERROTA')
    elif pla == 3:
        print('VITORIA')
    elif pla == 4:
        print('VITORIA')
    elif pla == 5:
        print('DERROTA')
    else:
        print('Jogada invalida')
elif pc == 'papel':
     if pla == 1:
        print('vitoria')
     elif pla == 2:
        print('empate')
     elif pla == 3:
        print('derrota')
     elif pla == 4:
        print('vitoria')
     elif pla == 5:
         print('derrota')
     else:
        print('Jogada invalidaa')
elif pc == 'pedra':
     if pla == 1:
        print('perdeu')
     elif pla == 2:
        print('ganhou')
     elif pla == 3:
        print('empatou')
     elif pla == 4:
        print('perdeu')
     elif pla == 5:
        print('ganhou')
     else:
        print('Jogada invalidasss')
elif pc == 'lagarto':
     if pla == 1:
        print('ganhou meu nobre!')
     elif pla == 2:
        print('perdeu meu chapa')
     elif pla == 3:
        print('ganhou meu nobre')
     elif pla == 4:
        print('empatado my nobre')
     elif pla == 5:
        print('perdeu meu nobre')
     else:
        print('Jogada invalidaaaaa')
elif pc == 'spock':
     if pla == 1:
        print('Spock esmaga tesoura(perdeu)')
     elif pla == 2:
        print('Papel refuta Spock(ganhou)')
     elif pla == 3:
        print('Spock vaporiza pedra(perdeu)')
     elif pla == 4:
        print('Lagarto envenena Spock(ganhou)')
     elif pla == 5:
        print('Empatou')
     else:
        print('Jogada invalida')