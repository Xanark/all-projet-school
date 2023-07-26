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
        self.premier:list=Maillon()
    

    def est_vide(self):
        return self.premier.suivant is None and self.premier.valeur is None


m1=Maillon(12,None)


liste=Liste()
if liste.est_vide():
    print("quelque chose")