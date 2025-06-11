class Racas:
    def __init__(self, nome, vida, forc, const, dest, sabe, inte, mana):
        self.nome = nome
        self.vida = vida
        self.forc = forc
        self.const = const
        self.dest = dest
        self.sabe = sabe
        self.inte = inte
        self.mana = mana
    def apresentar(self, raca):
        print(f'Ola {self.nome}. Percebi que você é um {raca}!\nVou mostrar seus atributos!')
        print(f'Vida: {self.vida}\nForça: {self.forc}\nConstituicao: {self.const}\nDestreza: {self.dest}\nSabedoria: {self.sabe}\nInteligencia: {self.inte}\nMana: {self.mana}')


class Anao(Racas):
    def __init__(self, nome):
        super().__init__(nome, vida=124, forc=18, const=14, dest=10, sabe=13, inte=11, mana=69)

class Draconato(Racas):
    def __init__(self, nome):
        super().__init__(nome, vida=150, forc=18, const=12, dest=9, sabe=15, inte=10, mana=88)

class Elfo(Racas):
    def __init__(self, nome):
        super().__init__(nome, vida=114, forc=15, const=18, dest=15, sabe=9, inte=11, mana=60)

class Humano(Racas):
    def __init__(self, nome):
        super().__init__(nome, vida=130, forc=13, const=13, dest=13, sabe=13, inte=13, mana=13)

class Orc(Racas):
    def __init__(self, nome):
        super().__init__(nome, vida=180, forc=18, const=10, dest=9, sabe=10, inte=10, mana=50)

class Tiefling(Racas):
    def __init__(self, nome):
        super().__init__(nome, vida=110, forc=12, const=14, dest=15, sabe=18, inte=17, mana=88)

class Gnomo(Racas):
    def __init__(self, nome):
        super().__init__(nome, vida=100, forc=10, const=18, dest=18, sabe=11, inte=12, mana=60)