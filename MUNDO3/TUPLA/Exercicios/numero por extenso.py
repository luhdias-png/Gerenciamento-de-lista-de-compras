num =  ('zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    valida = int(input('Digite um numero de 0 a 20:\n'))
    if valida >20:
        print('Excedeu o numero. Tente novamente! Numeros apenas de 0 a 20.')
        continue
    elif valida < 0:
        print('Numeros negativos invalidos! Tente novamente! Numeros apenas de 0 a 20.')
    else:
        print(f'Voce digitou o numero {num[valida]}')
        break