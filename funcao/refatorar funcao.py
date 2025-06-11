#Refatorar = Editar o codigo.
#----------------------------------------------------------------------------------------------------------------------------------------------
#Digamos que vc ja tenha colocado sua funcao que seria a SOMA(x,y) e esta funcionando direito. Mas gostaria de colocar o z para somar 3 numeros
'''
def soma(x,y):  ok  | def soma(x,y,z):
    print(x + y)    |    print(x + y + z)
soma(5,5)           |soma(5,5) Erro nos codigos com com 2 somas ja que o Z nao foi inserido na leitura
'''
#Poderiamos resolver passando o valor de z=0 a funcao original, e editar ou adicionar todos os codigos de printados dando o valor de z=?
'''
def soma(x,y,z=none):
    if z is not none:
        print(f'{x=} {y=} {z=}', x + y +z)
    else:
        print(f'{x=} {y=}, x + y)
'''
#Colocamos um sistema de condicoes, caso o valor de z for falso(ou seja sem valor) ele ira ignorar sem quebrar os codigos de apenas 2 digitos
#Ja se tiver valor no z mesmo que seja 0, mostrara no resultado mostrando o seu valor, que nesse caso poderia ser 0 ou qlqer numero.
