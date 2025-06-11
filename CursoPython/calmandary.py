while True:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um segundo numero: '))
    op = input('Digite um operador: (+,-,*,/) ')
    num_validos = None
    try:
        num1 = float(n1)
        num2 = float(n2)
        num_validos = True
    except ValueError:
        num_validos = None
    if n1 in num_validos is None:
        print('O primeiro Numero esta invalidos! Tente novamente!')
        continue
    elif n2 in num_validos is None:
        print('O segundo numero esta invalido! Tente novamente! ')
        continue
    operadores = '+-*/'
    if len(op) > 1:
        print('Operação invalida! Tente de novo!')

    if op == '+':
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é: {soma}')
        menu = input('Deseja continuar ou sair? [S/N]:').strip().upper()
        if menu == 'S':
            continue
        else:
            break
    elif op == '-':
            soma = n1 - n2
            print(f'A subtração de {n1} e {n2} é: {soma}')
            menu = input('Deseja continuar ou sair? [S/N]:').strip().upper()
            if menu == 'S':
                continue
            else:
                break
    elif op == '*':
        soma = n1 * n2
        print(f'A Multiplicaão de {n1} e {n2} é: {soma}')
        menu = input('Deseja continuar ou sair? [S/N]:').strip().upper()
        if menu == 'S':
            continue
        else:
            break
    
    elif op == '/':
        soma = n1 / n2
        print(f'A divisao de {n1} e {n2} é: {soma}')
        menu = input('Deseja continuar ou sair? [S/N]:').strip().upper()
        if menu == 'S':
            continue
        else:
            break


    sair = input('Deseja sair?[S/N]: ').strip().upper().startswith('S')
    if sair is True:
        break