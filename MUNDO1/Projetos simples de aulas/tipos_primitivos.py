L = (input('Digite algo:'))
print('Qual é o classe da escrita?', type(L)) #define o tipo da escrita(toda funcao é crtzdo como STR. Para mudar deve converter antes do input.)
print('Só tem espacos?', L.isspace()) #define se tem espacos
print('É numerico?', L.isnumeric()) #define se é numerico (apenas numeros)
print('É Alfabetica?', L.isalpha())#define se é alfabetico (apenas letras)
print('É alfanumerico?', L.isalnum())#define se se tem letras E numeros.
print('Esta em Maiusculas?', L.isupper())#define se toda escrita esta em maiusculo
print('Esta em minusculas?', L.islower())#define se toda escrita esta em minusculo
print('Esta capitalizada?', L.istitle())#define se a primeira letra esta em maiusculo
print('Tem acentos?', L.isascii())#Retorna True se todos os caracteres pertencem à tabela ASCII (sem acentos, emojis, ou caracteres não ingleses).
