p = float(input('Digite o valor do preco: R$'))
d = int(input('Digite o desconto dado: '))
preco = p*d/100
i = p - preco

print(f'O valor de R${p} fica por R${i:.2f}, com {d}%. O desconto no preco foi de R${preco:.2f}')