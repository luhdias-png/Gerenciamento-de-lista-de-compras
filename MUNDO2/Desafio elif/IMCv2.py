import time

cor = {'limpa':'\033[m',
         'vermelho':'\033[;31m',
         'verde': '\033[;32m',
         '_': '\033[4m',
         'negrito':'\033[1m',
         'laranja':'\033[;33m',
         'branco':'\033[;37m'}

print(f'{cor["verde"]}-={cor["limpa"]}'*25)
print(f"{'Calculadora de IMC':=^50}")
print(f'{cor["verde"]}-={cor["limpa"]}'*25)

peso = int(input('Digite seu peso:'))
alt = float(input('Digite sua altura:'))
imc = peso / (alt**2)
time.sleep(1)
print('Calculando...')
time.sleep(1)
print(f'Seu IMC esta de {imc:.2f}. Significa que voce esta:', end=' ')
if imc < 18.5:
    print('Voce esta magro demais. Precisa de nutrientes!')
elif imc >=18.5 and imc <=24.9:
    print('Voce esta no peso ideal. Parabens!')
elif imc >= 25 and imc <= 29.9:
    print('Voce esta acima do peso. Faça exercicios e procure um dieta.')
elif imc >= 30 and imc <= 34.9:
    print('Voce esta com OBESIDADE nivel 1. Procure um medico')
elif imc >=35 and imc <= 39:
    print('Voce esta com OBESIDADE NIVEL 2. Procure um medico COM URGENCIA!!!')
else:
    print(f'{cor["vermelho"]}RISCO DE VIDA ALTA!{cor["limpa"]}')