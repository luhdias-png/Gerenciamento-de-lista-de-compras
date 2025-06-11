#codigo extraido de aluno Luiz Para analise e estudo.


from time import sleep
from random import randint
itens = ('Pedra' ,  'Papel' , 'Tessoura')
comp = randint(0 , 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESSOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[34mJO')
sleep(0.9)
print('KEN')
sleep(0.9)
print('PO\033[m')
sleep(0.9)
print('O computador jogou {}'.format(itens[comp]))
print('O jogador jogou {}' .format(itens[jogador]))
if jogador == 2 and comp == 0:
    print('\033[1;31mCOMPUTADOR GANHOU\033[m ')
elif jogador == 1 and comp == 2:
    print('\033[1;31mCOMPUTADOR GANHOU \033[m')
elif jogador == 0 and comp == 1:
    print('\033[1;31mCOMPUTADOR GANHOU\033[m')
elif comp == 0 and jogador == 1:
    print('\033[1;32mJOGADOR GANHOU\033[m')
elif comp == 1 and jogador == 2:
    print('\033[1;32mJOGADOR GANHOU\033[m')
elif comp == 2 and jogador == 0:
    print('\033[1;32mJOGADOR GANHOU\033')
elif comp == jogador:
    print('\033[7;33mEMPATE\033[m')