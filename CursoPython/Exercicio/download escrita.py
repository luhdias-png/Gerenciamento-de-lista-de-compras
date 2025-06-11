import time, os

def progressao(porcento, largura=40):
    cheio = int(porcento * largura / 100)
    barra = '█' * cheio + '-' * (largura - cheio)
    print(f'[{barra}] {porcento}%',end='\r',flush=True)


def digita(texto, vel=0.2):
    for i in texto:
        time.sleep(vel)
        print(i, end='', flush=True)

print('='*30)
print(f"{'Download manager':=^30}")
print('='*30)

while True:
    print('Deseja efetuar o download de que:\n[1]Video do youtube\n[2]Musica do youtube\n[3]Hackzao')
    try:
        menu = int(input(':'))
        if menu == 1:
            os.system('cls')
            digita('Operacao validada!\n', vel=0.055)
            digita('...\n', vel=1)
            time.sleep(2)
            digita('Efetuando Download:\n', vel=0.066)
            for i in range(101):
                time.sleep(0.10)
                progressao(i)
            print('\nDownload concluido!\n')
            print('Video baixado com sucesso.\n0% de error.\n100% arquivo limpo.')
    except ValueError:
        os.system('cls')
        print('Operação invalida. Use apenas numeros.')
        continue