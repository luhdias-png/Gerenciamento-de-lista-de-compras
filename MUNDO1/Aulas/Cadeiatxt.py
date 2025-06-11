txt = ('  Curso em Video Python  ')

print('A frase tem:', txt.replace('Python', 'Android'))#substituiu o 'python pelo android.
print('A frase tem', txt.find('s'))# Encontra uma letra ((Preciso aprender +))
print('A frase tem:', txt.capitalize())# Deixa apenas a primeira letra da frase em Maiusculo
print('A frase tem:', txt.title())# Deixa todas as iniciais da frases em Maiusculo
print('A frases tem:', txt.split())# separa em listas(['Curso', 'em', 'Video', 'Python'])
print('A frase tem:', txt.strip())# exclui espaços no comeco e fim da frase.
print('A frase tem:', txt.rstrip())#Tirar os espacos da direita.
print('A frase tem:', txt.lstrip())#tirar os espaços da esquerda.
print('A frase tem:', '-'.join(txt))#separa cada letra com o que é colocado antes do ''.join(variavel):(- -C-u-r-s-o- -e-m- -V-i-d-e-o...)

