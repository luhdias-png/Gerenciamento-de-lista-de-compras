import random
import os
pc = 0
v = 0
while pc != 1:
    print('-='*25)
    print('Vamos brincar de impar ou par')
    print('-='*25)
    usuanum = int(input('Digite um numero:'))
    pcnum = random.randint(0,10)
    decisao = input('Deseja escolher Par ou Impar[I/P]').strip().upper()
    total = usuanum + pcnum
    par = total %2 == 0
    if par:
        print(f'O usuario: {usuanum}\nO Computer: {pcnum}\nRESULTADO: {total} = PAR!!')
        if decisao == 'P':
            print('Jogador venceu!')
            v += 1
        else:
            print('Computador venceu!')
            pc += 1
    else:
        print(f'O usuario: {usuanum}\nO Computer: {pcnum}\nRESULTADO: {total} = IMPAR!!')
        if decisao == 'I':
            print('O Jogador que escolheu IMPAR venceu')
            v += 1
        else:
            print('Computador venceu!(decisao no impar)')
            pc += 1
print(f'O jogador conseguiu vencer {v}x!')
