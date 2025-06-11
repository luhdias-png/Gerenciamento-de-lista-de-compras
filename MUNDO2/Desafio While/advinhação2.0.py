import random
import time
print('='*51)
print(f'{"jogo da advinhação 2.0":=^51}')
print('='*51)
pc = random.randint(1,10)
num = 0
chance = 0
print('Vou pensar em um numero\nTENTE ADIVINHAR!')
time.sleep(1)
print('Pronto?')
while num != pc:
    num = int(input('digite o numero eu pensei:'))
    chance +=1
    if num == pc:    
        print(f'Voce \033[1;32mCERTOU\033[m!!! Eu pensei no numero{pc}')
        break
    else:
        time.sleep(1)
    print('Voce \033[1;31mERROU\033[m!!! Tente de novo.')
print(f'Voce teve {chance} numeros de tentativa pra ganhar!')