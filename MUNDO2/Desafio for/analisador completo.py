tot = 0
maiorh = 0
nomeh = ''
totm = 0
for c in range(1,5):
    print(f'{f"{c}PESSOA":=^13}')
    nome = input('Nome:').strip().upper()
    idade = int(input('Idade:'))
    sexo = input('Sexo [M/F]:').strip().upper()
    tot += idade
    if c == 1 and sexo in 'M':
        maiorh = idade
        nomeh = nome
    if sexo in 'M' and idade > maiorh:
        maiorh = idade
        nomeh = nome
    if sexo in 'F' and idade < 20:
        totm += 1
media = tot / 4
print(f'A media de idade deles sao de: {media}.')
print(f'O homem mais velho se chama {nomeh} e sua idade é {maiorh}.')
print(f'Ao todo sao {totm} com menos de 20 anos.')