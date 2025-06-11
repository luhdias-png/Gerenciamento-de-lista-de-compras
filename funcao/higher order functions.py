def saudacao(msg, *nome):
    return f'{msg}, para o {nome}'

def executa(funcao,*args):
    return funcao(*args)


v = executa(saudacao,'ola meu nobre','td bem?','me chamo sonic','tenho',1.56,'metros e tenho', 31,'anos meu nobre')

print(v)

def sonic():
    return 'mandei bem?'

s = sonic

print(lambda :s)

sonic()