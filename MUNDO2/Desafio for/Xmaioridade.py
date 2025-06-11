import datetime
dat = datetime.date.today().year
totma = 0
totme = 0
for c in range(1,8):
    idd = int(input(f'Digite seu ano de nascimento da {c} pessoa: '))
    ano = dat - idd
    if ano >=21:
        totma+= 1
    else:
        totme += 1
print(f'Tivemos {totma} pessoas maiores de idade.')
print(f'Tivemos {totme} pessoas menores de idade.')
#treinar