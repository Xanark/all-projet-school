"""
Leo Dumas
novembre 2022
"""


class Arbre:

    def __init__(self, val=None, g=None, d=None):
        self.valeur=val
        self.gauche=g
        self.droite=d
    

    def get_valeur(self):
        return self.valeur

    def get_gauche(self):
        return self.gauche

    def get_droite(self):
        return self.droite

    def insere_droite(self, val):
        self.droite = Arbre(val, None, self.droite)
    
    
    def insere_gauche(self, val):
        self.gauche = Arbre(val,self.gauche, None )




def hauteur(n):
    if n==None:
        return 0
    elif n.droite==None and n.gauche==None:
        return 1
    else:
        return hauteur(n.gauche) + hauteur(n.droite)




racine = Arbre("A")
print("l'hauteur de l'arbre est", hauteur(racine))
racine.insere_gauche("B")
racine.insere_droite("F")
noeud_B=racine.gauche
noeud_B.insere_gauche("C")
noeud_B.insere_droite('D')
noeud_F = racine.droite
noeud_F.insere_gauche('G')
noeud_F.insere_droite('H')
noeud_C = noeud_B.gauche
noeud_C.insere_droite('E')
noeud_G = noeud_B.gauche
noeud_G.insere_droite('I')
noeud_H = noeud_B.gauche
noeud_H.insere_droite('J')
print("l'hauteur de l'arbre est", hauteur(racine))

