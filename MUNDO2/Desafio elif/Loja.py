print('-='*25)
print(f'{"Loja do Mandary":=^50}')
print('-='*25)

din = int(input('Qual o valor da sua compra:'))
print('Digite a forma de pagamento: ''\n[1]A vista no pix!(desconto de 10%)\n[2]A vista do Cartão(desconto de 5%).\n[3]Parcela 2x no Cartao(sem juros).\n[4]Parcela 3x ou mais no cartao(20% juros).')
pag = int(input(' '))
if pag == 1:
    des = din - (din * 10 / 100)
    print(f'Sua compra de R${din:.2f} ganha 10% de desconto passando a ser R${des:.2f}.')
elif pag == 2:
    des = din - (din * 5 / 100)
    print(f'Sua compra de R${din:.2f} A VISTA no cartao ganha 5% de desconto passando a ser R${des:.2f}.')
elif pag == 3:
    des = din /2 
    print(f'Sua compra de R${din:.2f} parcelado em 2x no cartao fica a ser 2x de R${des:.2f}.')
elif pag == 4:
    tot = din + (din * 20/100)
    vez = int(input('Quantas vezes quer pagar:'))
    des = tot / vez 
    print(f'Sua compra de R${din:.2f} pagando no cartao em {vez}x fica: {vez}x de R${des:.2f} um total de R${tot:.2f}!')

