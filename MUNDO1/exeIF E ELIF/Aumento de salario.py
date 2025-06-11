sal = float(input('Digite seu salario para ganhar um aumento:R$'))

if sal > 1250:
    gan = sal * 10/100
if sal < 1250:
    gan = sal *  15/100

print(f'Seu salario de R${sal:.2f} passa a ser:\nR${sal + gan:.2f}!')