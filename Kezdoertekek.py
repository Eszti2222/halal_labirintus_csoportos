import random

class Kezdoertekek:
    def __init__(self, nev:str, szint:int):
        self.nev = nev
        self.szint = szint
        self.allapot = "Alaphelyzet"

    def __str__(self):
        return f"Az érték neve: {self.nev}, A szintje: {self.szint}" 

    def ertekadas():
        dobas_ugyi:int=int(random.random()*6+1)
        dobas_elet:int=int(random.random()*6+1)
        dobas_elet2:int=int(random.random()*6+1)
        dobas_szer:int=int(random.random()*6+1)

        ugyesseg:int=dobas_ugyi+6
        eletero:int=dobas_elet+dobas_elet2+12
        szerencse:int=dobas_szer+6
        
        ertekek=["Ügyesség", "Életerő", "Szerencse"]
        szintszam=[ugyesseg, eletero, szerencse]


    