"""
Leo Dumas
septembre 2022
"""

class Maillon :

    def __init__(self,valeur=None,suivant=None):
        self.valeur=valeur
        self.suivant=suivant
        

m1=Maillon(12,None)

print(m1.valeur,m1.suivant)