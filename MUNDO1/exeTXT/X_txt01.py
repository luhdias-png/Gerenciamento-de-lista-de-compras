n1 = input('Digite seu nome completo: ').strip()#.strip() precisa de parênteses
print('Analisando seu nome...')
print(f'Seu nome em maiusculo fica: {n1.upper()}')
print(f'Seu nome em minusculo fica: {n1.lower()}')
print(f'Seu nome contem {len(n1) - n1.count(" ")}')# Quando você usa aspas simples para a f-string e também dentro dela, o Python se confunde.
print(f'tem {n1.find(" ")} letras no seu primeiro nome')


#Treinar mais isso. :(