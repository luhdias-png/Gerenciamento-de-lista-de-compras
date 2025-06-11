#O programa deve inserir, deletar e checar os indicis da lista.
lista = []

print(f'{"Lista de Compras":=^30}')
while True:
    print('='*25)
    menu = int(input('Digite o que deseja:\n[1]Adicionar itens na lista.\n[2]Excluir algo da lista\n[3]Checar a lista.'))
    print('='*25)
    if menu == 1:
        valor = input('Digite o que deseja adicionar a sua lista: ')
        if valor not in lista:
            lista.append(valor)
        else:
            print('Esse nome ja esta na lista.')
            continue
    elif menu == 2:
        if not lista:
            print('A lista ta vazia seu animal')
            continue
        try:
            valor = int(input(f'Digite um valor de 0 a {len(lista)-1} para excluir!'))
            if 0 <= valor < len(lista):
                remover = lista.pop(valor)
                print(f'O item \033[1;4;31m{remover}\033[m foi excluido com sussexo')
            else:
                print('Indice invalido')
        except ValueError:
            print('Seu burroooooo')
    elif menu == 3:
        if not lista:
            print('A lista esta vazia')
            continue
        print('os itens na lista sao:')
        for i, item in enumerate(lista):
            print(f'{i} - {item}')
    elif menu == 4:
        print('Graças a Deus isso acabou')
        break