'''
Nome: André Lucas Dias
Materia:Python
Prof: Caio
Turma: 3003
'''
#Gerenciar uma lista de compras com adição, visualização, alteração e exclusão de itens, incluindo desconto e cálculo total.   28/10/2025

from os import system
from time import sleep

#=====FUNCOES AUXILIARES=====#
def ler_input(mensagem, tipo=str, obrigatorio=True):
#Permite que leia entrada do usuario obrigando, ou nao, que algo seja escrito. Pedindo se necessario que o usuario coloque de a escrita
#de forma correta com a utilizacao do Int, Float e etc.
    while True:
        valor = input(mensagem).strip()
        if not valor:
            if obrigatorio:
                print("Campo obrigatório. Tente novamente.")
                continue
            else:
                return None
        try:
            return tipo(valor)
        except ValueError:
            print(f"Valor inválido. Esperado tipo {tipo.__name__}.")
            
def continuar():
#Permite o usuario a opcao de continuar com a opcao anterior ou saia dela permitindo um code mais limpo sem repeticao de code.
    while True:
        try:
            opc = int(input("Deseja continuar?\n[1]SIM/[2]NAO\n:"))
            if opc not in[1,2]:
                print("Valor invalido! Apenas use o 1 para SIM ou 2 para NAO.")
                continue
            return opc == 1
        except ValueError:
            print("Digite apenas numeros.")
#=============FIM DAS FUNCOES AUXILIARES======================#
            
#=============FUNCOES DOS MENUS===============================#

def menu():
#Apenas para exibir o menu do programa.
    while True: 
        system('cls')
        print("="*50,f"{'Lista de compra':=^50}","="*50, sep="\n")   
        print("[1]Adicionar item.\n[2]Mostrar lista.\n[3]Alterar lista.\n[4]Excluir lista.\n[0]Sair.")
        escolha = ler_input(":",int,obrigatorio=True)
        if escolha in [0,1,2,3,4,5]:
            return escolha
        else:
            print("Entrada invalida. Escolha do 0 ao 5.")
            sleep(2)
#-----------------------------------------------------------------------------------------------------------------------------------------------
def add_1(lista):
#Permite o usuario cadastrar os itens com precos quantidades e descontos em um dicionario para cada indice na lista.
    system('cls')
    while True:
        nome = ler_input("Qual o nome do item: ",str).capitalize()
        while True:
            valor = ler_input("Quanto custa: R$",).replace(",",".")
            if valor.isalpha():
                print('Use numeros e separe os centavos com "," ou ".".')
                continue
            else:
                valor = float(valor)
                break
        qtd = ler_input("Quantidade de peças: ", int)
        desconto = ler_input("Desconto (%): ", float, obrigatorio=False) or 0.0
        registro = {"Nome_item":nome,
                "Preco":valor,
                "Quantidade":qtd,
                "Desconto":desconto}
        lista.append(registro)
        if not continuar():
            break
#-----------------------------------------------------------------------------------------------------------------------------------------------
def mostrar(lista, pausar=True, titulo=True):
#Permite mostrar os itens cadastrados na lista, com a opcao de pausar na tela se desejar e exibir o titulo.
    system('cls')
    if not lista:
        print("Lista esta vazia.")
        if pausar:
            input("Aperte ENTER para sair.")
        return

    if titulo:
        print(" ","="*84,f'{"MINHA LISTA":^84}'," ","="*84,sep="\n")
    
    print(f" {'Índice':^6} | {'Nome':^20} | {'Preço':^10} | {'Qtd':^6} | {'Desconto':^10} |","-"*84, sep="\n")
    total_geral = 0
    for i, item in enumerate(lista, start=1):
        desconto =  item['Desconto'] if item['Desconto'] else 0
        total = item['Quantidade'] * item['Preco'] * (1- desconto / 100)
        print(f"{i:^6} | {item['Nome_item']:<20} | R$ {item['Preco']:>8.2f} | {item['Quantidade']:^6} | {desconto:>8.2f}% | TOTAL = R$ {total:.2f}\n","="*84)
        total_geral += total
    print("TOTAL DOS ITENS","="*58,f"R$ {total_geral:.2f}" )
    if pausar:
        input("Aperte ENTER para continuar.")
    return
#-----------------------------------------------------------------------------------------------------------------------------------------------
def alterar(lista):
#Permite o usuario alterar algum valor da lista.
    system('cls')
    if not lista:
        print("Lista esta vazia")
        sleep(2)
        return
    system('cls')
    mostrar(lista, pausar=False, titulo=False)
    mudar = ler_input('Digite um Numero do indice para alterar os valores ou "0" para sair:', int)
    if mudar == 0:
        print("Operacao cancelada!")
        sleep(2)
        return
    elif 0 < mudar <= len(lista):
        item = lista[mudar -1]
        
        item['Nome_item'] = ler_input("Novo nome:",obrigatorio=True).capitalize() or item['Nome_item']
        
        while True:
            preco_str = ler_input("Novo preco: ",str,obrigatorio=True)
            if not preco_str:
                break
            preco_str = preco_str.replace(",",".")
            if preco_str.replace(",",".").isalpha():
                print('Use apenas números e separe os centavos com "," ou ".".')
                continue
            else:
                item['Preco'] = float(preco_str)
                break    
        
        qtd = ler_input("Nova quantidade: ",int, obrigatorio=True)
        if qtd is not None:
            item['Quantidade'] = qtd
            
        desconto = ler_input("Novo desconto: ",int, obrigatorio=False) 
        if desconto is not None:
            item['Desconto'] = desconto  
            
        print("\nItem atualizado com sucesso!")     
                    
    else:
        print("Indice não achado.")
        sleep(2)
#-----------------------------------------------------------------------------------------------------------------------------------------------
def excluir(lista):
#Permite o usuario excluir todo o item do dicionario de um indice da lista atualizando o seu valor total.
    system('cls')
    if not lista:
        print("A lista esta vazia")
        sleep(2)
        return
    system('cls')
    while True:
        system('cls')
        mostrar(lista, pausar=False, titulo=False)
        delete = ler_input("Digite o numero do indice da lista.\n Digite [0] para sair.\n:",int, obrigatorio=False)
        if delete == 0:
            print("Operacao cancelada!")
            sleep(2)
            break
        if 0 < delete <= len(lista):
            system('cls')
            confirmar = ler_input(f"Deseja deletar:\nNome:{lista[delete -1]['Nome_item']} | Valor: R${lista[delete -1]['Preco']:.2f} |Quantidade: {lista[delete -1]['Quantidade']} | Desconto: {lista[delete -1]['Desconto']:.2f}%\n[1]SIM/[2]NAO\n:",int)
            if confirmar == 1:
                lista.pop(delete -1)
                print("Item excluido com sucesso.")
                sleep(2)
                if not continuar():
                    break
            else:
                print("Operacao cancelada")
                sleep(2)
        else:
            print("Valor invalido.")
            sleep(2)
#-----------------------------------------------------------------------------------------------------------------------------------------------   
#=====Fim da Funcao de adicionar item na lista=====#
def main():
# Lista principal onde todos os itens serão armazenados
    lista = []
    while True:
        system('cls')
        opcao = menu()
        if opcao == 0:
            break
        elif opcao == 1:
            add_1(lista)
        elif opcao == 2:
            mostrar(lista)
        elif opcao == 3:
            alterar(lista)
        elif opcao == 4:
            excluir(lista)
    print("Obrigado por usar o My List")    
    
main()