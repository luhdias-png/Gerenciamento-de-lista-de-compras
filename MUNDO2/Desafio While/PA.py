print('='*40)
print(f"{'10 Termos de uma PA':=^40}")
print('='*40)

n1 = int(input('Digite a primeira progreção:'))
n2  = int(input('Digite a Razao:'))
termo = n1
con = 1
while con <=10:
    print(f'{termo} → ',end='')
    termo+=n2
    con += 1