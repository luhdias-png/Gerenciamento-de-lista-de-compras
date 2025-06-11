cores = {'limpa':'\033[m',
         'vermelho':'\033[;31m',
         'verde': '\033[;32m',
         '_': '\033[4m',
         'negrito':'\033[1m',
         'laranja':'\033[;33m',
         'branco':'\033[;37m'}

print(f'{cores["vermelho"]}-{cores["limpa"]}{cores["branco"]}='*25)
print(f"{'Emprestimo SANTOANDRÉ':=^50}")
print(f'{cores["vermelho"]}-{cores["limpa"]}{cores["branco"]}='*25)

vc = float(input('Digite o valor da casa:R$ '))
sal = float(input('Digite o seu salario:R$ '))
x1 = int(input('Digite quanto tempo vc quer pra pagar a casa: '))
an = x1 * 12
t1 = vc / an


if t1 >= 0.3 * sal:
    print(f'{cores["vermelho"]}{cores["negrito"]}Seu emprestimo {cores["_"]}NÃO{cores["limpa"]}{cores["vermelho"]}{cores["negrito"]} foi aprovado!{cores["limpa"]}')
    print(f'{cores["vermelho"]}{cores["negrito"]}Voce teria que pagar {cores["_"]}R${t1:.2f} por {x1} ano(s){cores["limpa"]}')
else:
    print(f'{cores["verde"]}{cores["negrito"]}{cores["_"]}SEU CREDITO ESTA APROVADO{cores["_"]}!')
    print(f'Voce tera que pagar R${t1:.2f} em {x1} ano(s).')
print(f'{cores["vermelho"]}-{cores["limpa"]}{cores["branco"]}='*25)
print(f"{'Emprestimo SANTOANDRÉ':=^50}")
print(f'{cores["vermelho"]}-{cores["limpa"]}{cores["branco"]}='*25)