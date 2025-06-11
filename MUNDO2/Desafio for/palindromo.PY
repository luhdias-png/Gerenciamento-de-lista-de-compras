txt = input('Digite um texto:').replace(' ','').upper()
ive = ''
for c in range(len(txt)-1,-1,-1):
    ive += txt[c]
if txt == ive:
    print(f'O {txt} ao contrario fica:\n{ive}.\nELA É PALINDROMO')
else:
    print(f'ela nao é palindromo.\n{txt} ao contrario fica\n{ive}.')