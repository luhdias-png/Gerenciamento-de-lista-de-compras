import random
import time #Comando para fazer o python esperar um pouco.

pc = random.randint(0,5)

print(f"{'Game de adivinhar':-^50}")
print('Vou pensar em um numero de 0 a 5. Tente adivinhar')
time.sleep(2)
print('pensando...')
time.sleep(3)
num = int(input('Qual o numero eu pensei: '))
if num <= 5:
    if num == pc:
        time.sleep(2)
        print(f'Isso eu pensei no "{pc}".')
    else:
        print('Vc errou! bwahahahaha')
else:
    print('Digite um numero de 5 pra baixo animal.')

print(f"{'FIM':-^50}")

