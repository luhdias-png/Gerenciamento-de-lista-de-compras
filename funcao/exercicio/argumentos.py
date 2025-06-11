def multiplicar(*args):
    total = 1
    for num in args:
        total *= num
    return total

numero = multiplicar(10,2,3,4,5)

print(numero)
#=============================================================================================================================================

'''def vezes(*args):
    total = 1
    for num in args:
        total *= num
    return total

num2 = 1

while True:
    menu = int(input('===MENU===\n[0]Para sair.\n[1]Para continuar.\n:'))
    if menu == 1:
        while True:
            numeros = int(input('Digite um numero:'))
            num2 = vezes(num2, numeros)
            print(f'O numero "{num2}" esta sendo multiplicado por "{numeros}"/nVeja o que esta acontecendo em "vezes"{vezes }')
            continua = int(input('Deseja continuar?\n[0]NAO.\n[1]SIM\n:'))
            if continua == 1:
                continue
            else:
                break
    else:
        break

print(num2)'''
#===========================================================================================================================================

def par (*args):
    for numero in args:
        if numero %2 ==0:
            print (f'O numero "{numero}" é Par')
        else:
            print(f'O numero {numero} é impar')
    return numero


par(4)
#=============================================================================================================================================

def par_impar (numero):
    multiplo_numero = numero% 2 ==0
    
    if multiplo_numero :
        return f'{numero} é par'
    else:
        return f'{numero} é impar'
    
print(par_impar(14))

#=============================================================================================================================================


def redondo_if (numero):
    multiplo_numero = numero% 2 ==0
    
    if multiplo_numero :
        return f'{numero} é par'
    return f'{numero} é impar'
    
print(f'redundancia do if e else {redondo_if(25)}')