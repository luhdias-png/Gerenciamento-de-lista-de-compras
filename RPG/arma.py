from random import randint

class Armas:
    def __init__(self, nome, propriedade, dano, tipo, elemento="nenhum", danoelem= 0):
        self.nome = nome
        self.propriedade = propriedade
        self.dano = dano
        self.tipo = tipo
        self.elemento = elemento
        self.danoelem = danoelem
    def mostrar(self):
        print(f'{self.nome} ela é uma arma {self.propriedade} tem um dano de {self.dano} com um tipo de {self.tipo} e {'tem elemento' if self.elemento != "nenhum" else 'nao tem elemento'}')
        if self.elemento != "nenhum":
            print(f"O elemento é {self.elemento}")
        else:
            None

class Cajado_de_Gelo(Armas):
    def __init__(self, nome="Cajado do inferno"):
        super().__init__(nome=nome, propriedade="uma mão", dano=randint(10,15), tipo="concussao", elemento="fogo",danoelem=randint(25,50))

class Espada(Armas):
    def __init__(self, nome="Espada longa", forc=10,):
        dano_base = randint(10,23)
        dano_final = (forc / 2) + dano_base if forc >= 18 else dano_base
        if dano_final >= 23: dano_final += randint (1,4) 
        super().__init__(nome=nome, propriedade="uma mão", dano=int(dano_final), tipo="cortante", elemento="nenhum", danoelem=0,)
