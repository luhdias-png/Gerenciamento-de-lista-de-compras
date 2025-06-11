menu = 0
num1 = int(input('Digite um valor:'))
num2 = int(input('Digite o segundo valor: '))

while menu != 5:
    menu = int(input('O que quer fazer com os valores:\n[1]SOMAR\n[2]MULTIPLICAR\n[3]Maior\n[4]RETORNE OS VALORES\n[5]SAIR\n:'))
    if menu == 1:
        resultado = num1 + num2
        print(f'A soma de {num1} e {num2} é: {resultado}')
        novo = input('Deseja continuar [S/N]?').strip().upper()
        if novo == 'S':
            None
        else:
            break
    elif menu == 2:
        resultado = num1 * num2
        print(f'O resultado de {num1} multiplicado {num2} é: {resultado}')
        novo = input('Digite "S" para continuar. Qualquer tecla para sair.').strip().upper()
        if novo == 'S':
            None
        else:
            break
    elif menu == 3:
        if num1 > num2:
            print(f'O numero {num1} é maior que o {num2}.')
        elif num1 == num2:
            print('Os numero sao iguais')
        else:
            print(f'O numero {num1} é menor que o {num2}.')
        novo = input('Deseja continuar [S/N]?').strip().upper()
        if novo == 'S':
            None
        else:
            break
    elif menu == 4:
        print('Digite os numeros de novo.')
    elif menu == 5:
        print('Obrigado por usar meu programa')
        break
    else:
        print('Pedido invalido. Tente de novo.')
print('fim')