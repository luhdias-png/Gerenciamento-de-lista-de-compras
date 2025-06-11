s = float(input('Digite o salario:R$ '))
a = int(input('Digite a valor da porcentagem do aumento:'))
preco = s*a/100
sa = s + preco
print('='*20)
print(f'O salario era de R${s} com aumento de {a}%.\fO salario passa a ser R${sa:.2f}.')
print('='*20)
print(f'Voce ganhou {preco:.2f} de aumento.')
