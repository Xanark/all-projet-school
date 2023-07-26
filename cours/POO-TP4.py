"""
Leo Dumas
septembre 2022
"""


class Voiture :
   
    def __init__(self, marque:str="",cylindrée:int=0):
        self.marque = marque
        self.cylindrée=cylindrée
    
        
    def taxe(self):
        if self.cylindrée<=1600:
            return "300 euro"
        elif self.cylindrée>1600 and self.cylindrée>=2300:
            return "500 euro"
        else : 
            return "700 euro"

    def get_info(self):
        return (self.marque ,self.cylindrée,)

class Flotte :

    def __init__(self, flotte:list=[]):
        self.flotte = flotte

    def ajouter(self,v):
        self.flotte.append(v)

    def affiche(self):
        return (self.flotte)
    
    def taxe(self):
        if self.flotte<=1600:
            return "300 euro"
        elif self.flotte>1600 and self.flotte>=2300:
            return "500 euro"
        else : 
            return "700 euro"
    
    def taxe_tot(self):
        for i in range(len(self.flotte)):
            a+=(self.flotte(i)).taxe()
        return a 

v1=Voiture("toyota",1598)
v2=Voiture("BMW", 2756)
print(v1.get_info())
Flotte().ajouter(v1)
Flotte().ajouter(v2)
print(Flotte().affiche())
print(Flotte().taxe_tot)