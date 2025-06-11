contador = 0

while contador <= 99:
    contador += 1
    if contador %2:
        print(contador)
        continue
    if contador == 20:
        break

    print(f'{contador} ← esses sao pares ')

print('ACABOU')