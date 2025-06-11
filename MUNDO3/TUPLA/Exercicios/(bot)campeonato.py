#limpo do chat gpt

import os, time

brasileirao = ('Palmeiras','Red Bull Bragantino','Flamengo','Cruzeiro','Fluminense','Bahia',
    'Ceará','Corinthians','Internacional','Atlético Mineiro','São Paulo','Botafogo',
    'Grêmio','Fortaleza','Vasco da Gama','Santos','Juventude','Mirassol','Sport','Vitória')

while True:
    print('Digite o que deseja ver:\nA) Apenas os cinco primeiros colocados\nB) Os últimos 4 colocados\nC) Times em ordem alfabética' \
          '\nD) Em que posição está o São Paulo')
    menu = input(': ').strip().upper()

    if menu == 'A':
        os.system("cls")
        for i, time_ in enumerate(brasileirao[:5], start=1):
            print(f"{i})- {time_}")
        print()
        time.sleep(2)

    elif menu == 'B':
        os.system('cls')
        for i, time_ in enumerate(brasileirao[16:], start=17):
            print(f"{i})- {time_}")
        print()
        time.sleep(2)

    elif menu == 'C':
        os.system('cls')
        print(' - '.join(sorted(brasileirao)))
        print()
        time.sleep(2)

    elif menu == 'D':
        pos = brasileirao.index("São Paulo") + 1
        print(f'O São Paulo está na {pos}ª posição.')
        time.sleep(2)

    else:
        print('Opção inválida, tente novamente.')
        time.sleep(2)
