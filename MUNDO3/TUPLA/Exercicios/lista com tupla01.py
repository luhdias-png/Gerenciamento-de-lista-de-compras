lista = ('SONIC',5,'TAILS',2,'KNUCKLES',6,'METAL SONIC',5,'SUPER SONIC',25.50,'SHADOW',75.50,'ROUGE',15.5)

for i in range(0,len(lista)):# Para colocar uma variavel em range, deve primeiro converter em numeros.Usamos a funcao len
    if i % 2 == 0:# Usando o i (indice) para separar os indices pares dos impares(ja que a lista ta par=preco/impar=nome)
        print(f'{lista[i]:.<20}',end='')# {lista[i]}O i foi colocado para remover o () da tupla e pegar apenas o que foi colocado em cada indice.

    else:
        print(f'R${lista[i]:>6.2f}')#O numero que voce coloca conta com a quantidade de letras que ja tem na str.
#ex:'ola mundo'=ola mundo(8,0 SEMPRE É CONTADO), Caso queria alinhar para a esquerda para ficar:
#(..ola mundo) basta fazer = print('ola mundo':.>2)[:(iniciar formatacao do conteudo)>(alinha valor da direita< para a esquerda>)
#9(define um espaco de 9 caracteres, incluindo o que ja esta.)]