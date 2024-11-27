import random

class Kezdoertekek:
    def __init__(self, ugyesseg:int, eletero:int, szerencse:int):
        self.ugyesseg = ugyesseg
        self.eletero = eletero
        self.szerencse = szerencse
        self.allapot = "Alaphelyzet"
        ugyesseg:int=0
        eletero:int=0
        szerencse:int=0
        print(ugyesseg)

    def kezdes(self, ):
        self.allapot = "Kezdés"
        dobas_ugyi:int=int(random.random()*12+1)
        dobas_elet:int=int(random.random()*12+1)
        dobas_elet2:int=int(random.random()*12+1)
        dobas_szer:int=int(random.random*12+1)

        ugyesseg:int=dobas_ugyi+6
        eletero:int=dobas_elet+12
        szerencse:int=dobas_szer+6
