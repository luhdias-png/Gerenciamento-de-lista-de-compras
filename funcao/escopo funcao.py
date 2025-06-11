#Escopo em Python é o espaço ou contexto onde uma variável está visível e pode ser usada.
#Ou seja, onde você pode acessar aquela variável — depende de onde ela foi criada.

#A variavel x=1 esta fora do escopo (ou caixa) da funcao 'caixa' no momento ela esta sendo imutavel, ou seja, o valor dela nao sera alterada.
x = 1
print('-'*150)
print('Inicio de escopo com variaveis dentro de escopos/funcoes')
print('-'*150)
def caixa():
    x= 15
#No escopo 'caixa' outra variavel x=15 foi colocada, porem nao influencia a primeira variavel ja esta dentro do escopo funcao'caixa'.
#cada variavel dentro de uma funcao é unica, ou seja, mesmo com mesmo nome nao influencia a que esta fora, exceto se houver uma funcao...
#chamada "global" para unir variaveis fora do escopo.
    def funcao():
#aqui foi criado outra funcao dentro de uma funcao com uma variavel x=11, novamente falando ela esta aqui como se fosse a primeira variavel...
#... ou seja as variaveis x= 1 e x=15 nao a influenciam nem a mudam, essa variavel é unica e exclusiva do escopo 'funcao' sem mudar as de fora.

        x=11
        y=2
        print(x,y)#vai printar a funcao que recebeu o nome 'funcao' ou seja, vai printar x=11 e y=2
    funcao()#aqui vai chamar para ser exibida a funcao do escopo 'funcao' dentro do escopo 'caixa' para ser exibida.
    print(x)#aqui vai printar o x dentro do escopo 'caixa' que é x=15

#Fora de todo os escopos/funcoes sera printado normalmente:
caixa()#Aqui sera printado o que esta dentro da funcao 'caixa' que é: x=11 y=2(q foi o que esta escrito no escopo funcao) e x= 15 dentro do...
#..Escopo funcao.
print(x)#a variavel criada fora de funcao nenhuma.
print('Acabou o exemplo de variaveis dentro de escopos/funcoes')
print('-'*150)
#=============================================================================================================================================
#Usando o global para unir as variaveis.
#Aqui vamos usar um exemplo que variaveis mutaveis(ou seja que mudam seus valores) dentro de funcoes.
#Aprendemos anteriormente que variaveis dentro de funcoes nao comunica com variaveis fora da funcao, mas tem uma excecao. Se a palavra-chave
#GLOBAL estiver em um escopo chamando a variavel que esta fora dela, ele a substitui com a nova dentro do escopo podendo alterar, somar ou
#atibuir qlqer coisa nela.

a=1#variavel sendo chamada
def sonic():
    global a #global esta unindo a variavel de fora com a de dentro
    a=5 #aqui a variavel a foi unida com a de fora da funcao recebendo o valor 5
    def shadow():
        global a #Agora o global esta unindo a variavel que era 5 da funcao 'sonic' para se tornar o q a funcao 'shadow' quiser.
        a+=10 #Agora a variavel a que era 5 foi somado com a propria variavel a foi atribuida aqui do valor 10 ou seja 5 + 10 = 15 'a' passa
# a ser a=15 ja que foi somado os valores.
        b=2 #b permanece local até ser tornado global por global b".
        def tails():
            a = 7
            global b            #ISSO É UMA MA PRATICA USAR GLOBAL PARA UNIR, MUDAR OU COMUNICAR COM A VARIAVEL EXTERNA!!!
            b = 6
            print(a,b)
        tails()
        print(a,b)
    shadow()
    print(a)
sonic()
print(a)
