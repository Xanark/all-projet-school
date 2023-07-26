"""
Leo Dumas
septembre 2022
"""



#exercice 1:

class Carte :
    nbre_cartes=0
    def __init__(self, val=0, coul=""):
        self.valeur = val
        self.coul=coul
        Carte.nbre_cartes+=1

    def get_attributs(self):
        return (self.valeur, self.coul)
        



cart1 =Carte(4,"trèfle")
cart2 =Carte(10,"coeur")


print(cart1.get_attributs())
print(cart2.get_attributs())
print(id(cart1)==id(cart2))
print(Carte.nbre_cartes)


#exercice 2:

class Domino():
    nbre_domino = 0
    def __init__(self, face1=0, face2=0):
        self.face1 = face1
        self.face2= face2
        Domino.nbre_domino+=1

    

    def get_valeurs(self):
        return (self.face1, self.face2)
        
    def set_valeurs(self, val1, val2):
        self.face1=val1
        self.face2=val2
        return(self.face1, self.face2)
        

    def affiche_points(self):
        return (self.face1, self.face2)

    def somme(self):
        return (self.face1 + self.face2)

domino1 =Domino(2,3)
domino2 =Domino(4,6)


print(domino2.get_valeurs(),domino1.get_valeurs())
print(domino2.somme()+ domino1.somme())
print(domino2.set_valeurs(2,5))
print(domino2.affiche_points())
print(domino2.somme()+ domino1.somme())