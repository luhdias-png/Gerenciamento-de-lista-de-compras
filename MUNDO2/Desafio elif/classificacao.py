from datetime import date
import emoji


ano = int(input('Digite seu ano de nascimento:'))
hj = date.today().year
idade = hj - ano




if idade >=31:
    print('VOCE É ANCIAO!!!')
elif idade >= 25 and idade <=30:
    print(f'Voce tem {idade} anos.\n Voce recebeu a classificao de MESTRE')
elif 20<= idade <=24:
    clas = 'SENIOR'
    print(f'Seu ano de nascimento é:{idade}\nSua classificação é {clas}!')
elif 17 <= idade <=19:
    clas = 'PLENO'
    print(f'Seu ano de nascimento é:{idade}\n Sua classificação é {clas}!')
elif 14 <=  idade <= 16:
    print(f'Seu ano de nascimento é:{idade}\nSua classificação é ABORRECENTE')
elif idade >=10 and idade <=13:
    print(f'Seu ano de nascimento é:{idade}\nSua classificação é KID')
else:
    print(f'muito novo vc tem {idade} ano')

