num = int(input('Digite um numero: '))
u = num // 1% 10
d = num // 10% 10
c = num // 100% 10
m = num // 1000% 10

print(f'Analisando o seu numero:{num}')
print(f'Seu numero tem {u} Unidade.')
print(f'Seu numero tem {d} Dezena.')
print(f'Seu numero tem {c} Centena')
print(f'Seu numero tem {m} milhar.')
#treinar isso