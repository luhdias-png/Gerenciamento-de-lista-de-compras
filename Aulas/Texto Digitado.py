import time
print('Digite algo para escrevermos:\n')
texto = input('')

oi = 'oi'

def digitar(texto):
    for i in texto:
        print(i, end='', flush=True)
        time.sleep(0.2)

print(f'Voce digitou isso:\n{oi}')


digitar(texto)

