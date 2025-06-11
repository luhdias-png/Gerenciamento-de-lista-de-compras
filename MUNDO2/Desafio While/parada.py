num = con = soma = 0
num = int(input('Digite um numero ou [999] para sair e ver o resultado.'))
while num != 999:
    soma += num
    con += 1
    num = int(input('Digite um numero ou [999] para sair e ver o resultado.')) 
    
print(f'Voce digitou {con} numeros, a soma deles é de {soma}.')