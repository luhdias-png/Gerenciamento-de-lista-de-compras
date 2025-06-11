'''for lucas in range(4):#Ultimo numero sempre é ignorado. (de 0 a 5 = 01234)(de 5 a 10 = 56789).
    print(lucas)
print('fim')'''
#===============================================================================================================================================
#contagem regressiva usando o for fica assim:
'''for lucas in range(6,0,-2):#Sintaxe geral do range(início, parada, passo):início (6): O valor inicial da contagem.
                           #parada (0): O valor onde a contagem vai parar (mas sem incluir esse número).
                           #passo (-1): O valor que será subtraído a cada iteração (cm o passo é negativo, estamos contando para trás).
                           #passo (-1): Se colocar -2 ou 2 ele contaria de 2 em 2 ou subtrairia de 2 em 2 
    print(lucas)
print('fim')'''

#===============================================================================================================================================
#Usando variaveis para usalas dentro de range(aqui dentro)
'''i = int(input('Inicio:'))
fim = int(input('FIM:'))
passo = int(input('PASSO:'))

for cah in range(i, fim+1, passo):#As variaveis de input foram colocar em repeticoes.
    print(f'{cah}')#cah vai ser o que vai contar'''
#===============================================================================================================================================
#Usando Variaveis com input DENTRO da range.
'''for mon in range(0,3):
    n = int(input('Digite um numero:'))
print('fim')'''
#===============================================================================================================================================
#Usando variaveis para somar todo o que o usuario digitar em loop.
s = 0
for luh in range(3):
    n = int(input('Digite um numero:'))
    s += n
print(f'O resultado dos numeros somado é: {s}')