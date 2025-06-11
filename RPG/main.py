import classes

nome = input('Qual é o seu nome:')

raça = int(input("Qual raça vc deseja ser:\n[1] Anão.\n[2] Draconato.\n[3] Elfo."))
if raça == 1:
    personagem = classes.Anao(nome)
    raca = 'Anão'
elif raça == 2:
    personagem = classes.Draconato(nome)
    raca = 'Draconato'
elif raça == 3:
    personagem = classes.Elfo(nome)
    raca = 'Elfo'
else:
    print("Erro!")

personagem.apresentar(raca)