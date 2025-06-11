num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))

if  num1 > num2:
    print(f'O numero:"{num1}" é MAIOR que {num2}.')
elif num1 < num2:
    print(f'O numero:"{num2}" é MAIOR que {num1}')
elif num1 == num2:
    print('Os numeros sao iguais.')