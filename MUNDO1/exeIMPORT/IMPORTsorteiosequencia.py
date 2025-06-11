import random
p1 = str(input('Digite um nome: '))
p2 = str(input('Digite um nome: '))
p3 = str(input('Digite um nome: '))
p4 = str(input('Digite um nome: '))
p5 = str(input('Digite um nome: '))
lista = [p1, p2, p3, p4, p5]
ran = random.shuffle(lista)

print(f'A sequencia sera: {lista}')