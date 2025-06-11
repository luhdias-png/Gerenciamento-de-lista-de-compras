n1 = int(input('\033[mDigite um numero: '))
tot = 0
for c in range(1,n1 +1):
    if n1 % c ==0:
        print('\033[36m',c,'\033[m',end='')
        tot += 1
    else:
        print('\033[31m',c,'\033[m',end='')
print(f'\nO numero {n1} foi divisivel {tot} vezes.')
if tot == 2:
    print('É por isso que ele é PRIMO.')
else:
    print('É por isso que ele NAO é PRIMO')