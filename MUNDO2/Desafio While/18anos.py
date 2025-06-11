n = 1
maior = 0
menor = 0
total = 0
while n != 0:
    n = int(input('Digite sua idade e digite "0" para sair:'))
    if n !=0:
        total +=1
        if n >= 18:
            maior += 1
        else:
            menor += 1
print(f'{total} pessoas foram registradas!\n{maior} maiores de idade.\n{menor} menores de idade!')
