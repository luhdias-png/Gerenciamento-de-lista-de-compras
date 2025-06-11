def ronaldo(a,b,c):
    print(a,b,c)#Aqui a funcao foi criada com parametros (a,b,c) pendindo para printar os paramentros

ronaldo(7,'vamo',2)#aqui ja é a execucao da funcao "ronaldo" dando "nomes" aos paramentros:a do paramentro da funcao = 7 um numero inteiro, 
#b do paramentro da funcao = uma str escrita "vamo" e por fim a c do paramentro da funcao = outro numero inteiro 
#------------------------------------------------------------------------------------------------------------------------------------------

ronaldo('ola mundo',7.00,"RPG")
#Nota que a funcao ronaldo foi chamado 2x, mas cada uma execultou pedidos diferentes graças aos parametros.Logo entendemos que nao precisa..
#.. de um valor fixo em cada paramentro, pode ser qualquer valor desde que o leitor aceite. nesse  caso uma string e numeros int e float.
#-------------------------------------------------------------------------------------------------------------------------------------------
def soma(x,y,z):#funcao soma chama os paramentros(X,Y,Z)
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)#Dentro da funcao chamamos um print para mostrar o que esta acontecendo dentro...
#... da funcao, aqui esta mostrando em F-String e dps a resolucao da funcao soma que é (x + y + z(AFINAL É UMA SOMA))
soma(1,2,3)#Aqui esta chamando a funcao somando os x,y,z com 1,2,3 dando o resultado de 6 (x=1,y=2,z=3)
soma(y=1, x=5, z=7)#Aqui soma esta sendo chamada porem dando nome aos parametros.A funcao equivale a 3 coisa (x,y,z) porem voce pode mudar a..
#..ordem dando comandos diretos a ela.Se executasse normal seria:x=1,y=5,z=7.Mas aqui mudamos a ordem para que Y receba 1 e X receba 5.
#Logo podemos mudar a ordem desde que informamos quais serao as ordens sem esquecer das outras.

print(soma(5,z=8, y=5))#A mesma coisa pode ser feita quando chamada por print.Printamos o que queremos, chamamos a funcao(que aqui é SOMA)...
#E colocamos o que queremos ser somado, se for padrao apenas SOMA e os numeros seriam o bastante, mas para melhor entendimento usamos o...
#paramentro nomeado para informar qual valor ser dado para cada parametro(soma 5[que é padrao o x],z=8[ao z foi dada o valor de 8] e ...
# y que foi dado o 5) Nota que o normal seria X, Y, Z, como o o Z foi colocado antes do Y, o paramentro Y precisou ser colocado para nao
#repetir o z.