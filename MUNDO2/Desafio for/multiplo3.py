soma = 0
cont = 0
for n1 in range(1,501,2):
    if n1 % 3 ==0:
        cont = cont + 1
        soma = soma + n1
print(f'A soma de todos os {cont} valores solicitados é {soma}')