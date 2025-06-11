nome = str(input('Digite seu nome: ')).strip()
nomes = nome.split()

print(f'Muito prazer em te conhecer: {nome}!\nSeu primeiro nome é: {nomes[0]}\nSeu ultimo nome é: {nomes[-1]}')
#por algum motivo o [-1] identifica o primeiro e ate o ultimo nome. caso a pessoa escreva 1 ou 500 nome ele vai pegar o primeiro e o ultimo.
#caso ele escreva apenas 1 Nome ele vai aceitar