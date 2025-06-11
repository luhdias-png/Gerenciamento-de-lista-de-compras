print('='*40)
print(f"{'10 Termos de uma PA':=^40}")
print('='*40)

if input('Antes de prosseguirmos, deseja saber o que é uma PA?(Progressao Aritmética)\nDigite [1] para saber ou outra tecla para prosseguir.') == '1':
    print('É uma sequencia de numeros reais, na qual cada termo anterior a partir do segundo é igual ao anterior somado a uma constante denominada: RAZAO.')
n1 = int(input('Primeiro TERMO: '))
n2 = int(input('Digite a RAZAO: '))
razao = n1 + (10 - 1) * n2
for c in range(n1, razao + n2, n2):
    print(c,end= ' → ')
print('FIM')