from random import choice
import time
print('-='*25)
print(f'{"JO KEN PO NERD":=^50}')
print('-='*25)

vs = ['tesoura', 'papel', 'pedra', 'lagarto', 'spock']
pc = choice(vs)
pla = vs[int(input('Digite:\n[0]TESOURA.\n[1]PAPEL.\n[2]PEDRA.\n[3]LAGARTO.\n[4]SPOCK.\n:'))]
#pegou algo da lista VS na posicao que o player digitou
#============================================================================================================================
#O input() exibe uma mensagem pedindo ao jogador para digitar um número de 0 a 4, representando as opções disponíveis.
#O valor digitado é convertido para int(), para ser usado como índice da lista 'vs'.
#O valor correspondente da lista 'vs' é armazenado na variável 'pla'.
#=============================================================================================================================

time.sleep(1)
print(f'Vamos ver quem ganha.')
print(f'Voce escolheu: {pla}')
print('-='*25)
print(f'O Computador escolheu: {pc}.')
print('-='*25)
if pc == 'tesoura' and pla == 'papel' or pla == 'lagarto':
    print('Pc ganhou.')
elif pc == 'papel' and pla == 'pedra' or pla == 'spock':
    print('PC ganhou.')
elif pc == 'pedra' and pla == 'tesoura' or pla == 'lagarto':
    print('PC ganhou.')
elif pc == 'lagarto' and pla == 'spock' or pla == 'papel':
    print('PC ganhou.')
elif pc == 'spock' and pla == 'tesoura' or pla == 'pedra':
    print('PC ganhou.')
elif pla == pc:
    print('EMPATOU')
else:
    print('player vence')#diz que o player ganha caso for o contrario