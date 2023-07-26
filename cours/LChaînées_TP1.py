"""
Leo Dumas
septembre 2022
"""


class Maillon :

    def __init__(self,valeur=None,suivant=None):
        self.valeur=valeur
        self.suivant=suivant


class Liste:

    def __init__(self):
        self.premier=Maillon()
    

    def est_vide(self):
        return self.premier.suivant is None and self.premier.valeur is None

    def ajoute(self,val=None):
        if self.est_vide():
            self.premier.valeur=val
        else: 
            self.premier=Maillon(val,self.premier)
         
    
    def affiche(self):
        self.affiche1 = self.premier
        while self.affiche1 is not None:
            print(self.affiche1.valeur)
            self.affiche1 = self.affiche1.suivant
    
    def longueur(self):
        a=0
        self.long = self.premier
        while self.long is not None:
            a+=1
            self.long = self.long.suivant
        return a

    def ajoute_fin(self,val2):
        if self.est_vide():
            self.premier.valeur=val2
        else: 
            self.premier=Maillon(val2,self.premier)
        


liste=Liste()
"""
liste.ajoute(5)
liste.ajoute(8)
liste.ajoute(12)
liste.affiche()

print(liste.longueur())
for i in range(9):
    liste.ajoute(i)
print(liste.longueur())
"""
liste.ajoute_fin(5)
liste.ajoute(4)
liste.ajoute_fin(12)
liste.affiche()
