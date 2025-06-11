#usando as cores de um outro jeito na versao f-string de um outro modolo.
#STYLE: 0(nada, none), 1 (negrito,bold), 4 (sublinhado, underline), 7 (inverter as cores, negative). tem mais a ser explorado
#TEXT: 30(cinza), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(ciano), 37(branco).Para usar mais que isso so com bibliotecas.
#BACK: Exatamente as mesmas cores do TEXT só que com o 40.

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
print(f'Vc tem {cor["roxo"]}{idade}{cor["limpa"]} anos.')
print(f'O jogo que voce gosta é {cor["vermelho"]}{jogo}{cor["limpa"]}.')
print(f'O curso que voce esta fazendo é {cor["bracopreto"]}{ti}{cor["limpa"]}.')