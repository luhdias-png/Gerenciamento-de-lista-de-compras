nome = str(input('Digite seu nome: ')).strip()
nomes = nome.split()

print(f'Muito prazer em te conhecer: {nome}!\nSeu primeiro nome é: {nomes[0]}\nSeu ultimo nome é: {nomes[-1]}')