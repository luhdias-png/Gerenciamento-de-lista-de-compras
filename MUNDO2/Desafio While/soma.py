n = 1
soma = 0
total = 0
while n !=0:
    n = int(input('Digite um numero ou 0 para parar.'))
    if n !=0:
        soma += 1
        total +=n
if soma > 0:
    div = total / soma
else:
    div = 0
print(f'Voce digitou {soma} vezes.\nOs resultados das {soma} foi de {total}\nA media deles foi de: {div}')
