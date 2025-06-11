nome = str(input('Digite seu nome completo: ')).lower().strip()
print(f'Seu nome é: {nome}')
if 'dias' in nome:
    print('Seu nome tem DIAS')
else:
    print('Seu nome NAO tem DIAS.')

