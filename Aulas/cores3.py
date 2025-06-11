#usando as cores de um outro jeito na versao f-string de um outro modolo.
#STYLE: 0(nada, none), 1 (negrito,bold), 4 (sublinhado, underline), 7 (inverter as cores, negative). tem mais a ser explorado
#TEXT: 30(cinza), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(ciano), 37(branco).Para usar mais que isso so com bibliotecas.
#BACK: Exatamente as mesmas cores do TEXT só que com o 40.
#-==-=-=-=-=-=--=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#no exemplo aqui foi feito varias variaveis e um dicionario; (dicionario em python == Um dicionário em Python é uma estrutura de dados...
#...  que armazena pares de chave-valor, onde cada chave é única e está associada a um valor. Ele permite o acesso aos valores...
#... de forma eficiente usando a chave correspondente.[exemplos: dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}])
# ; Onde foi usado palavras chaves para associar as cores do padrao ANSI assim podendo ser usado na f-string de maneira mais limpa.

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
jogo = input('Digite um game: ')
ti = input('digite um curso: ')
cor = {'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'vermelho': '\033[31m',
       'roxo': '\033[35m',
       'bracopreto':'\033[7;37m'}

print(f'Ola muito prazer em te conhecer {cor["azul"]}{nome}{cor["limpa"]}!!!')
#{cor==variavel:azul[a chave da cor:"azul" que ta o valor de \033[34. ]}{nome==variavelcomum}{cor==variavel:limpa[seria a chave dela:"limpa"...
#...com o valor de \033[m. ]}
print(f'Vc tem {cor["roxo"]}{idade}{cor["limpa"]} anos.')
print(f'O jogo que voce gosta é {cor["vermelho"]}{jogo}{cor["limpa"]}.')
print(f'O curso que voce esta fazendo é {cor["bracopreto"]}{ti}{cor["limpa"]}.')


#O que podemos aprender:
#Ao inves de poluirmos o codigo com o ANSI entre uma palavra ou outra, pode ser usado um dicionario para atribuir valores que queremos dar...
#...as palavras. Criar uma lista com ma variavel e dar palavras chaves com valores para retornar.