# Exercice 1

'''
class Pile():
    """
    Permet de créer une pile avec une valeur et un suivant étant lui-même une pile
    """
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant

    def est_vide(self):
        return self.valeur is None

    def empile(self, nbr):
        if self.est_vide():
            self.valeur = nbr

        else:
            if self.suivant != None:
                self.suivant = Pile(self.valeur, Pile(self.suivant))
                self.valeur = nbr

            else:
                self.suivant = Pile(self.valeur)
                self.valeur = nbr

    def depile(self):
        if self.est_vide():
            return None

        else:
            val = self.valeur
            if self.suivant != None:
                self.valeur = self.suivant.valeur
                self.suivant = self.suivant.suivant
            
            else:
                self.valeur = None
                self.suivant = None

            return val

    def affiche(self):
        print(self.valeur)
        if self.suivant != None:
            self = self.suivant
            return self.affiche()

pile = Pile()
pile.affiche()
pile.empile(8)
pile.affiche()
pile.empile(-5)
pile.affiche()
pile.empile(18)
pile.affiche()
a = pile.depile()
print(a)
pile.affiche()
a = pile.depile()
print(a)
pile.affiche()
a = pile.depile()
print(a)
if pile.est_vide():
    print('la pile est vide')
a = pile.depile()
print(a)
'''


# Exercice 2

class Pile():
    """
    Permet de créer une pile avec une valeur et un suivant étant lui-même une pile
    """
    def __init__(self, p : list = [None]):
        self.nombres = p
        self.taille = len(p)

    def est_vide(self):
        return self.taille is None

    def empile(self, nbr):
        self.nombres.append(nbr)

    def depile(self):
        a = self.nombres.pop(0)
        return a

    def affiche(self):
        for i in range(self.taille):
            print(self.nombres[i])

pile = Pile()
pile.affiche()
pile.empile(8)
pile.affiche()
pile.empile(-5)
pile.affiche()
pile.empile(18)
pile.affiche()
a = pile.depile()
print(a)
pile.affiche()
a = pile.depile()
print(a)
pile.affiche()
a = pile.depile()
print(a)
if pile.est_vide():
    print('la pile est vide')
a = pile.depile()
print(a)