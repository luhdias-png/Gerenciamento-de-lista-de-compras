'''
metodos uteis com lista.
para adicionar algo no final da lista: lista.append()
para adicionar um item NO INDICE ESCOLHIDO: lista.insert()
para remover algo da lista: lista.remove()
para remover algo no final ou no indice escolhido: lista.pop()
para apagar um INDICE: del lista
para limpar a lista: lista.clear
para extender a lista: lista.extend
'+' ou '-' concatena a lista
'''
#------------------------------------------------------------------------------------------------------------------------------
'''
lista = ['lucas','danilo','mona']
lista.append('Outro')
nome = lista.pop()
print(lista,nome)
'''

lista = []
while True:
    nome = input('Digite algo para por na lista: ').strip().upper()
    lista.append(nome)
    print(lista)
    dele = input('Deseja remover algum nome? ["N" para cancelar]: ').strip().upper()
    if dele == 'N':
        continue
    else:
        if dele not in lista:
            print('Nao achamos o que pediu.')
            print(lista)
            continue
        if dele in lista:
            lista.remove(dele)
            print(lista)
            continue
    