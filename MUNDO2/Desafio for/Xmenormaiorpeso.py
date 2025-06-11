totma = 0
totme = 0
for c in range(1,6):
    p = float(input(f'Digite o peso da {c} pessoa: '))
    if c ==1:
        totma = p
        totme = p
    else:
        if p > totma:
            totma = p
        if p < totme:
            totme = p
print(f'O maior peso lido foi de KG{totma}')
print(f'O menor peso lido foi de KG{totme}')
#treina muito