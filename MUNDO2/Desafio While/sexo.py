m = 0
f = 0
while True:
    s = input('Digite "M" ou "F" para registrar o sexo, e "S" para sair:').strip().upper()[0]#Usando o [] pega apenas a quantidade de letra usado na frase.
    if s == 'M':
        m += 1
    elif s == 'F':
        f += 1
    elif s == 'S':
        break
    else:
        print('Comando invalido')
        s = input('Digite "M" ou "F" para registrar o sexo, e "S" para sair:').strip().upper()
print(f'Foi registrado {m} Pessoas com o sexo masculino e {f} pessoas com sexo feminino')