soma = 0
cont = 0
for n1 in range(1,7):
    n2 = int(input(f'Digite o {n1} valor: '))
    if n2 % 2 == 0:
        soma += n2
        cont += 1
print(f'Voce informou {cont} numeros, e a soma dos numeros pares é {soma}.')
