cidade = str(input('digite uma cidade que vc nasceu: ')).lower().strip()#logica de programação(primeiro ele vai deixar minusculo e dps remover espaços)

if 'santo' in cidade[:5]: #Se tiver: 'santo' na variavel cidade, conte apenas as 5 letras.
    print('verdadeiro') #vai retornar o valor verdadeiro pq deve ter: 'santo' na palavra.
else:#se nao tiver so vai dar falso
    print('falso')

#APRENDIDO MAS A MELHORAR