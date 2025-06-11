media = quat = soma = maior = menor =  0 
menu = 'S'
while menu in 'S':
    n1 = int(input('Digite um numero:'))
    menu = input('Deseja continuar?[S/N]').strip().upper()[0]
    soma += n1
    quat += 1
    if quat ==1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = soma / quat
print(f'Voce digitou {quat} e a media deles é de {media:.2f}.')
print(f'O maior numero foi {maior} e o menor numero foi {menor}')