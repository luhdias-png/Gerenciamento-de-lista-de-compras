import emoji
import time

print(emoji.emojize('Vamos analisar se a medida que vc vai dar sera um triangulo:\n:régua_triangular:EQUILATERO, ISÓCELES ou ESCALENO:régua_triangular:.', language='pt'))

esc = int(input('Digite [1] para saber o que significa cada triangulo ou [0] para seguir.'))
time.sleep(2)
if esc == 1:
    print('-='*25)
    print('Triangulo EQUILATERO:"Todos os lados devem ser iguais"\nTriangulo ISÓCELES:"Apenas dois lados iguais"\nTriangulo ESCALENO:"Todos os lados diferentes".')
    time.sleep(2)
    print('-='*25)
elif esc == 0:
    print('vamos prosseguir.')
    time.sleep(2)
    print('-='*25)

r1 = int(input('Digite a primeira medida:'))
r2 = int(input('Digite a segunda medida:'))
r3 = int(input('Digite a terceira medida:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Eles PODEM fazer um triangulo.')
    if r1 == r2 == r3:
        print(f'A medida de {r1} e {r2} e {r3} formam um triangulo EQUILATERO!')
    elif r1 != r2 != r3 != r1:#Se A é diferente de B e B é diferente de C, C e A podem ser iguais. por isso certifique de prestar atenção em TODAS as igualdades/diferencias.
        print(f'A medida de {r1} e {r2} e {r3} formam um triangulo ESCALENO!')
    else:#Para nao perder tempo aqui ele ja assume que A é diferente de B e B é diferente de C mas que C pode ser igual a A.
        print(f'A medida de {r1} e {r2} e {r3} formam um triangulo ISÓCELES!')
else:
    print('Eles NAO PODEM fazer um triangulo.')