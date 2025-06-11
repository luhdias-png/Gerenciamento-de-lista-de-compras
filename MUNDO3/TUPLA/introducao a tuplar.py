# Criando uma tupla (imutável) chamada "lanche"
# Essa forma abaixo é equivalente a: lanche = ('hamburguer', 'suco', 'bolo', 'sorvete')
lanche = 'hamburguer', 'suco', 'bolo', 'sorvete'

# Acessando um item específico da tupla pelo índice
print(lanche[2])  # Mostra o item no índice 2: 'bolo'

# Fatiando a tupla: do índice 1 ao 2 (o índice final não é incluído)
print('Mostrando do jeito de escolhas, do indice x ao indice y.', lanche[1:3])
# Isso imprime: 'suco' e 'bolo' (índices 1 e 2)

print('='*50)

# ------------------------- FORMA 1: Usando "for item in tupla" -------------------------
# Percorrendo a tupla e exibindo cada item
for food in lanche:
    print(f'Eu vou comer {food}')
print('Comi muito!')

print('='*50)

# Exibindo os itens da tupla em uma linha, separados por hífen
for comida in lanche:
    print(f'{comida}', end="-")  # Atenção: é necessário colocar vírgula antes do end=
print()  # Quebra de linha após o loop
print('='*50)

# ------------------------- FORMA 2: Usando "for i in range()" -------------------------
# Mostrando os índices com range e len()
for i in range(0, len(lanche)):
    print(i)  # Mostra apenas os números dos índices (0, 1, 2, 3)

print('='*50)

print('FOR e(indice) IN RANGE(0, LEN(lanche)):')
# Exibindo os itens da tupla e suas posições usando o índice
for e in range(0, len(lanche)):
    print(f'Forma organizada com fatiamento:\n{lanche[e]} < (item da tupla) na posição {e}')

print('='*50)

# ------------------------- FORMA 3: Usando "enumerate()" -------------------------
# enumerate() retorna tanto o índice quanto o valor ao mesmo tempo
print('Aqui foi usado FOR posicao, item IN ENUMERATE(lanche):')
for posicao, lula in enumerate(lanche):
    print(f'Eu vou comer muita {lula} na posição: {posicao}')

print('='*50)
#--------------------------- FORMA 3: Usando "sorted"-----------------------------------
#sorted() retorna os itens da tupla de forma organizada, nao por numeros, mas em ordem alfabetica
print(sorted(lanche))
#====================================================================================================================================
# OUTRAS FORMAS DE MEXER COM TUPLAS

# Criando duas tuplas com diferentes tipos de dados (inteiros, strings, float)
a = 1, 2, 3, 4, 5, 'ola', 0.5, 'hello world'
b = 6, 7, 8, 'thau', 0.10, 'bye world'

# Exibindo as duas tuplas separadamente
print(a, b)

# Unindo as tuplas a e b em uma nova tupla chamada c (sem alterar as originais)
c = a + b
print(c)

# Mostrando quantos elementos existem dentro da tupla c
print(len(c))  # Deve mostrar 14 elementos

# Contando quantas vezes o número 5 aparece na tupla c
print(c.count(5))  # Deve retornar 1, pois o 5 aparece uma vez

# Mostrando em qual posição (índice) está o valor 8 dentro da tupla c
print(c.index(8))  # Deve mostrar a posição do número 8 na tupla c

# Buscando a posição do valor 2, mas começando a busca a partir do índice 4
print(c.index(4, 1))#  index(valor, início, fim)
#Onde está o número 4? O valor 4 está na posição 3. Como o Python está buscando?
#A busca começa do índice 1 em diante, ou seja, ele vai checar os itens a partir de 2 (índice 1), 3 (índice 2), 4 (índice 3)...
#Então o que acontece? O Python encontra o 4 no índice 3, mesmo começando a busca do índice 1.

#DIFERENÇA DA TUPLA DE PYTHON EM OUTRAS LINGUAGENS DE PROGRAMACAO: Ex: Java
#Como vimos antes, tuplas nao podem ser imutaveis e aceitam qualquer tipo de escrita (str, int, float), no caso de Java seria diferente.
#1- Em java nao se chama TUPLA, se chama VETORES que no caso nao permitem que adicione mais de uma escrita. Se for str, tem que ser ate o fim..
#nao é permitido adicionar mais de um tipo no mesmo vetor