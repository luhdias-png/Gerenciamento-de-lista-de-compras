import arma, classes
from random import randint
class Combate:
    def __init__(self, atacante, defensor, arma):
        self.atacante = atacante
        self.defensor = defensor
        self.arma = arma

        rolagem = randint(1,20)
        print=(f"Rolagem atacante: {rolagem}")
        if rolagem == 1:
            print(f"Falha critica! {nome} perdeu 25 de vida")
            self.atacante.vida -=25
            return
        
        if self.atacante.forc > self.defensor.dest:
            print("Ataque bem sucedido!")
            dano = self.arma.dano
            self.defensor.vida = dano
            print(f"O alvo recebeu {dano} de dano")
        else:
            print("Errou")