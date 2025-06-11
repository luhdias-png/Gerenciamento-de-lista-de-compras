m = 0
f = 0
homem = 0


while True:
    idade = int(input('idade:'))
    sexo = input('Sexo[M/F]:').strip().upper()[0]
    if sexo == 'M':
        homem += 1
        if idade >=18:
            m +=1
    elif sexo == 'F':
        if idade <20:
            f += 1
    continuar = input('Deseja continuar?[S/N]').strip().upper()
    if continuar == 'S':
        continue
    elif continuar == 'N':
        break
    else:
        print('Entrada invalida. Apenas M ou F')
        continue
print(f'Foram cadastrado {homem} Homens\n{m} sao maiores de 18\nE {f} sao mulheres com menos de 20 anos')