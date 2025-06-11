lista = ('Pao', 1.00,'Leite',5.55,'Placa de video',1950.00,'Jogo',250.00,'caderno',25.00,
         'Astarion',150.00,'Biscoito',3.00)
print('='*50)
print(f'{"LISTAGEM DE COMPRA":=^50}')
print('='*50)
for i in range(0,len(lista)):
    if i %2 ==0:
        print(f'{lista[i]:.<39}', end='')
    else:
        print(f'R${lista[i]:>9.2f}|')
print('='*50)