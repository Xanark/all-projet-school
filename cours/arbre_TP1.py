"""
Leo Dumas
novembre 2022
"""






class Arbre:

    def __init__(self,val=None, droit=None, gauche=None) -> None:
        self.val=val
        self.gauche=gauche
        self.droit=droit
    
    def get_valeur(self):
        print(self.val)
    def get_gauche(self):
        print(self.gauche)
    def get_droit(self):
        print(self.droit)


    def insere_droit(self, val1):
        if self.droit is None:
            self.droit=val1
        else:
            arbre2 = Arbre(val1)
            arbre2.droite = self.droit
            self.droite = arbre2

    def insere_gauche(self, val1):
        if self.gauche is None:
            self.gauche=val1
        else:
            arbre3 = Arbre(val1)
            arbre3.droite = self.droit
            self.droite = arbre3



racine = Arbre("A")
racine.get_valeur()
racine.get_droit()
racine.get_gauche()

racine.insere_gauche("B")
racine.insere_droit("F")

print(racine.get_droit())
print(racine.get_gauche())
print(racine.droit.get_valeur())
print(racine.gauche.get_valeur())


