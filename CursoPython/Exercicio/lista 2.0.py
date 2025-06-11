#lista de compras
import os, time

lista = []

print(f'{"LISTA DE COMPRAS":=^30}')
while True:
    print(f'{"MENU":=^30}')
    menu = int(input('Digite o que deseja adicionar na lista:\n[0] Adicionar item.\n[1] Excluir lista.\n[2] Ver lista.\n[3] Sair do programa.\n'))
    try:
        if menu == 0:
            os.system('cls')
            while True:
                print(f'{"ADICIONAR NA LISTA":=^50}')
                adicionar_lista = input('Digite algo para colocar na lista ou [0] para sair:\n').strip().capitalize()
                if adicionar_lista == '0':
                    os.system('cls')
                    break
                if adicionar_lista not in lista:
                    lista.append(adicionar_lista)
                    os.system('cls')
                    print('Item Adicionado.')
                else:
                    print(f'O item "{adicionar_lista}" ja foi adicionado.')
                    continue
                while True:
                    os.system('cls')    
                    retorno = input('Deseja adicionar mais item na lista?[0 = SIM/1 = NAO]\n')
                    if len(retorno) > 1:
                        print('Voce digitou mais de um caracter!')
                        time.sleep(2)
                        continue
                    try:
                        retorno = int(retorno)
                    except ValueError:
                        print('Digite apenas numeros')
                        time.sleep(2)
                        continue
                    if retorno > 1:
                        print('Sequencia de numeros invalidos.')
                        time.sleep(2)
                        continue
                    if retorno == 0:
                        os.system('cls')
                        break
                    elif retorno == 1:
                        os.system('cls')
                        break                
                if retorno == 1:
                    break
        elif menu == 1:
            os.system('cls')
            if not lista:
                print('A lista esta vazia')
                time.sleep(3)
                os.system('cls')
                continue
            print(f'{"LISTA":=^30}')
            for i, in range(0,len(lista)):
                print(f'{i:.<10}',end='')
                print(f'{lista[i]:.>16}')
            while True:
                delete = input('Digite o indice que deseja excluir ou [S] para sair:\n').strip().upper()
                if delete == 'S':
                    os.system('cls')
                    break
                try:
                    delete = int(delete)
                except ValueError:
                    print('Digite apenas numeros')
                    continue
                if delete < 0 or delete >= len(lista):
                    print('Esse indice nao esta na lista')
                    continue
                remover = lista.pop(delete)
                print(f'O item {remover} foi excluido com sucesso!')
                while True:
                    retorno = input('Deseja excluir outros itens?[0 SIM/1 NAO]\n')
                    if len(retorno) > 1:
                        print('Voce digitou mais de um caracter.')
                        time.sleep(2)
                        os.system('cls')
                        continue
                    try:
                        retorno = int(retorno)
                    except ValueError:
                        print('Digite apenas numero')
                        time.sleep(2)
                        os.system('cls')
                        continue
                    if retorno > 1:
                        print('Numeros invalidos')
                        time.sleep(2)
                        os.system('cls')
                        continue
                    if retorno == 0:
                        break
                    elif retorno == 1:
                        break
                if retorno == 1:
                    break
        elif menu == 2:
            os.system('cls')
            print(f'{"LISTA":=^30}')
            for i in range(0,len(lista)):
                print(f'{i:.<10}',end='')
                print(f'{lista[i]:.>16}')
            while True:
                retorno = input('Digite [0] para sair:\n')
                try:
                    retorno = int(retorno)
                except ValueError:
                    print('Digite apenas numeros')
                if retorno == 0:
                    os.system('cls')
                    break
                else:
                    print('Comando invalido')
                    continue
        elif menu == 3:
            os.system('cls')
            print('Obrigado por usar o programa.')
            break                              
    except ValueError:
        print('Digite apenas numeros!')