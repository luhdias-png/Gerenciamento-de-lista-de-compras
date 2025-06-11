import time

for i in range(101):
    time.sleep(0.1)
    print(f'Carregando: {str(i):.<4}%',end='\r')
print('acabou')

#========================================================================================================================

for i in range(100):
    time.sleep(0.1)
    print(f'🍎 Carregando: {i + 1:3d}%', end='\r')  # :3d deixa o número com largura 3, alinhado
print('\n✅ Acabou!')

#========================================================================================================================

def barra_progresso(porcentagem, largura=30):#porcetagem so recebe os numeros. A largura = 30 recebe quantos caracteres vai ter, nesse caso 30
    cheio = int(porcentagem * largura / 100)#Resultado: Multiplicamos a porcentagem pela largura(que é 30 char) / 100 (pra chegar em 100)
#exemplo, se a porcentagem for 30 vai multiplicar pelo largura (nesse caso 30) que vai dar 900 dividido por 100 vai dar 9 char.
# Ou seja 9 char serao preenchido de 30. 30% em uma barra com 30 espaços vai ocupar 9 espaços.
    barra = '█' * cheio + '-' * (largura - cheio)
    print(f'\r[{barra}] {porcentagem}%', end='', flush=True)#flush=True: força o Python a mostrar o print imediatamente (sem esperar).

for i in range(101):
    time.sleep(0.5)
    barra_progresso(i)
print('\nPronto!')

barra_progresso(50)

