#padrao ANSI = escape sequence. cogigos ANSI começam com "\" e dps o codigo.
#sempre que quiser colocar cor faça:\033[~~~M deve ser aberto em []Congetes[deve colocar 0,1,2 ou 3 codigos antes do M e dps do 033]
#1) Primeiro codigo vai ser o estyle = estilo[\033stylem] dps de colocar o codigo e querer acrescentar mais coloque o ";"
#2) Segundo vai ser para text = texto[\[033style;text].
#3) E por fim vai colocar a cor de fundo(back = background)[\[033style:text:back]
#Em primeiro lugar no style vc vai definir se vai estar em negrito, normal, italico ou sublinhado.
#Em segundo lugar vai informar em TEXT a COR DO TEXTO. E por ultimo a COR do FUNDO do texto (background)
#exemplo: \033(0[nao vai ter nada. o "0" nao tras nada com ele];33[TODAS AS CORES COMEÇA COM 30];44m
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-#
#STYLE: 0(nada, none), 1 (negrito,bold), 4 (sublinhado, underline), 7 (inverter as cores, negative). tem mais a ser explorado
#TEXT: 30(cinza), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(ciano), 37(branco).Para usar mais que isso so com bibliotecas.
#BACK: Exatamente as mesmas cores do TEXT só que com o 40.
#exemplo: Para deixar o fundo branco deve escrever o codigo assim: \033[7;30m [o 7 inverte a cor do background que esta 30(cinza)]

print('\033[1;33;31;0mola mundo')# a faixa vai ate o final da pagina.
print('\033[7;34mola mundos\033[m')#ao fim da escrita se colocar o \033[m ele vai encerrar as cores.
print('\033[1;35;42mola\033[4;33mMundinhos\033[m')
print('\033[7;37meae mundao blz?\033[m')
print('eae mundao blz?')

#pode ser usado tambem em f-string tambem abrindo e fechando {} antes de uma variavel.



nome = input('Digite seu nome:')

print(f'Ola muito prazer em te conhecer \033[1;4;36{nome}\033[m')