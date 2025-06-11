#Ordem dos valores aritimeticos:
# ()=os que estao em parenteses sempre em primeiro nao importao o sinal que estiver la dentro.
# **=os que tiver com potencia logo em seguida. ex (3+2)/ 5² ou 5**2= 5/25= 5.
# +, /, //, %= depois de ter os resultados dos 2 acima, o que tiver dps do resultado calcule com os sinais que pedem dentre esses 4.
# +, -= quando calcular todos e tiver algo para ser somado ou tirado, use-os. ###

# += soma 5+2 == 7
# -= menos 5-2 == 3
# *= multiplicação 5*2 == 10
# /= divisão 5/2 == 2.5
# **= potenciação 5**2 == 25
# //= divisao inteira == 5//2 == 2
# %= resto da divisao 5%2 == 1  ###

#!nome = input('qual o seu nome?')
#!print('Muito prazer{:^20}!'.format(nome))###

n1 = int(input('Digite um numero:'))
n2 = int(input('digite outro numero:'))
s = n1 + n2
m = n1 - n2
mu = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2

print(' A soma dos numero é:{}.\n Subtraindo eles ficam:{}.\n Mutiplicando é:{}.\n Dividindo é:{:.2f}.'.format (s, m, mu ,d), end='' )
print('\nQuando potencializa fica:{}.\n Dividindo inteiro é:{}.\n E o resto da divisao é:{}.'.format(p, di, r))