import random
import os
while True:
    lista = ['MENDOIM','MAÇA','LUCAS','MINHOCA','RUGIDO','LAIKA','ESTRANHO']
    palavra = random.choice(lista)
    tentativa = 0
    acerto =  ''
    while True:
        jogador = input('Digite uma letra para descobrir a palavra:\n').strip().upper()
        if len(jogador) > 1:
            print('Voce digitou mais de uma letra!')
            continue
        elif jogador.isdigit():
            print('Voce digitou numeros. A operação esta invalida!')
            continue    
        else:
            tentativa += 1
            if jogador in palavra:
                acerto += jogador
            else:
                print(f'A letra "{jogador}" NAO ESTA NA PALAVRA')
        mascara = ''        
        for lc in palavra:
            if lc in acerto:
                mascara += lc    
            else:
                mascara += '*'
        print(mascara)
        if mascara == palavra:
            os.system('clear')
            print(f'Parabens voce acertou a palavra!\nA palavra era:"{mascara}"\nVoce teve {tentativa} chances de acertar!')
            break
    menu = input('Quer continuar?[Sim para continuar, qualquer tecla para encerrar.]').strip().upper()[0]
    if menu == 'S':
        os.system('clear')
        continue
    else:
        print('Obrigado por jogar!')
        break