import os, time

brasileirao = ('Palmeiras','Red Bull Bragantino','Flamengo','Cruzeiro','Fluminense','Bahia',
    'Ceará','Corinthians','Internacional','Atlético Mineiro','São Paulo','Botafogo',
    'Grêmio','Fortaleza','Vasco da Gama','Santos','Juventude','Mirassol','Sport','Vitória')

while True:
    print('Digite o que deseja ver:\nA) Apenas os cinco primeiro colocados\nB)Os ultimos 4 colocados\nC)Os times em ordem alfabetica' \
    '\nD)Em que posicao esta SP')
    menu = input(':').strip().upper()
    if menu == 'A':
        os.system("cls")
        for i, time_ in enumerate(brasileirao[:5], start=1):#melhor forma de usar, com fatiamento.
            print(f"{i})- {time_}")
        print()
        time.sleep(2)
        os.system('cls')

    elif menu == 'B':
        os.system('cls')
        for i, time_ in enumerate(brasileirao[16:20], start=17):
            print(f"{i})- {time_}")
        print()
        time.sleep(2)
        os.system('cls')
        
    elif menu == 'C':
        os.system('cls')
        for i, time_ in enumerate(sorted(brasileirao)):
            print(time_, end=' - ')
        print()
        time.sleep(2)
        os.system('cls')

    elif menu == 'D':
        os.system('cls')
        print(f'O São Paulo esta na classificacao {brasileirao.index("São Paulo")+1}')
        time.sleep(2)
        os.system('cls')

    else:
        os.system('cls')
        print('Entrada invalida!')
        continue