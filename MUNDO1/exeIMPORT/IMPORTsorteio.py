import random
p1= str(input('Digite o primeiro nome: '))
p2= str(input('Digite o segunto nome: '))
p3= input('Digite o terceiro nome: ')
p4= input('Digite o quarto nome: ')
lista = [p1, p2, p3, p4] # lista em colchetes '[]' representa LISTAS em python
ran = random.choice(lista)

print(f'O escolhido foi voce: {ran}!')

