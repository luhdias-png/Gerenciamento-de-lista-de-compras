import emoji
import time

cor = {'neg':'\033[1m',
       '_': '\033[4m',
       'limpa':'\033[m',
       'azul': '\033[;34m',
       'roxo':'\033[;35m',
       'ciano':'\033[;36m'}

print(f'{cor["ciano"]}-={cor["limpa"]}'*25)
print(f"{'Conversor de Numeros':=^50}")
print(f'{cor["ciano"]}-={cor["limpa"]}'*25)
num = int(input('Digite um numero inteiro para ser convertido:'))
print(f'Digite:\n[1] para {cor["_"]}BINARIO{cor["limpa"]}.\n[2] para {cor["_"]}OCTA{cor["limpa"]}.\n[3] para {cor["_"]}HEXADECIMAL{cor["limpa"]}.')
op = int(input(''))
if op == 1:
       print('Convertendo em Binario...')
       time.sleep(2)
       print (emoji.emojize(f'Seu numero:{num} convertido em binario fica {cor["ciano"]}{cor["_"]}{bin(num)}{cor["limpa"]}:floppy_disk:'))
elif op == 2:
       print('Convertendo em OCTA...')
       time.sleep(2)
       print (emoji.emojize(f'Seu numero:{num} convertido em binario fica {cor["roxo"]}{cor["_"]}{oct(num)}{cor["limpa"]}:botão_de_setas_em_sentido_anti-horário:', language='pt'))
elif op == 3:
       print('Convertendo em Hexadecimal...')
       time.sleep(2)
       print (emoji.emojize(f'Seu numero:{num} convertido em binario fica {cor["azul"]}{cor["_"]}{hex(num)}{cor["limpa"]}:rosto_com_sobrancelha_levantada:', language='pt'))

print(emoji.emojize(':polegar_para_cima:Obrigado por usar nosso conversor:polegar_para_cima:!', language='pt'))
