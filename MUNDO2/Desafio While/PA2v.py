print('='*40)
print(f"{'10 Termos de uma PA':=^40}")
print('='*40)

n1 = int(input('Digite a primeira progreção:'))
n2  = int(input('Digite a Razao:'))
termo = n1
con = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while con <= total:
        print(f'{termo} → ',end='')
        termo += n2
        con += 1
    print('PAUSA')
    mais = int(input('Quantos termo voce quer mostrar a mais?'))
print('FIM')
