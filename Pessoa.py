class pessoa():

    def __init__(self,nome):
        self.nome = nome

    def falar(self,assunto):
        if self.comer:
            print(f'{self.nome}, não pode falar comendo')
            return
        print(f'{self.nome},esta falando {assunto}')
        return

    def parar_falar(self):
        if not self.falar:
            print(f'{self.nome}, não esta falando')
            return
        print(f'{self.nome}, parou de falar')
        self.falar = False
        return

    def comer(self,alimento):
        if self.falar:
            print(f'{self.nome}, não pode falar comendo {alimento}')
            return

        print(f'{self.nome}, está comendo {alimento}')
        return

    def parar_comer(self):
        if not self.comer:
            print(f'{self.nome},não esta comendo')
            return

        print(f'{self.nome}, parou de comer')
        self.comer = False
        return

    def bater_asa(self):
        if self.comer:
            print(f'{self.nome}, não pode bater asa comendo ')
            return
        if self.falar:
            print(f'{self.nome}, não pode bater asa falando ')
            return

        print(f'{self.nome} esta batendo asa')
        return

    def parar_bater_asa(self):
        if not self.bater_asa:
            print(f'{self.nome}, não esta batendo asa')
            return

        print(f'{self.nome}, parou de bater asa')
        self.bater_asa = False
        return