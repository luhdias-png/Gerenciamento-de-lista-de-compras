from datetime import date

nasc = int(input('Digite o ano que voce nasceu:'))
hj =  date.today().year
idade = hj - nasc


if idade > 18:
    saldo = idade - 18
    ano =  hj - saldo
    print(f'Voce tem {idade} anos. Voce deveria estar alistado em {ano}. ')
elif idade == 16 or idade == 17:
    saldo =  18 - idade
    ano = hj + saldo
    print(f'Voce tem {idade} anos. esta chegando a data se alistar! Voce deve alistar em {ano}')
elif idade <16:
    saldo = 18 - idade
    ano = hj + saldo
    print(f'Voce tem {idade} anos. ta cedo ainda para o alistamento. Voce deverar se alistar em {ano}!')
elif idade == 18:
    print(f'Voce tem {idade} anos. Seu ano de alistamento é {hj}!Vamo alistar!')