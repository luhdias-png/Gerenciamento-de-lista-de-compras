nome = str(input('Digite uma frase qualquer:')).lower().strip()
ver = str(input('Qual letra deve ser buscada: ')).lower().strip()

print(f'Sua frase é: "{nome}"!')
if ver in nome:
    print(f'A letra "{ver}" aparece {nome.count(ver)} vezes.')#Foi pedido pra ver quantas vezes a letra foi buscada em nome. pra isso foi usado a .count pra ver quantos (ver (letra)) tem em nome (variavel)
    print(f'A primeira letra "{ver}" na posição: {nome.find(ver) - nome.count(" ")}!')
    print(f'E a ultima letra "{ver}" apareceu na posição: {nome.rfind(ver) - nome.count(" ")}!')
else:
    print('Nao achamos essa letra!')

#A entender.
