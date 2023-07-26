"""
Leo Dumas
novembre 2022
"""
class Arbre():
    """Un arbre binaire"""

    def __init__(self, val = None, g = None, d = None):
        self.valeur = val
        self.gauche = g 
        self.droite = d

    def insere_droite(self, val):
        self.droite = Arbre(val, None, self.droite)

    def insere_gauche(self, val):
        self.gauche = Arbre(val, self.gauche, None)




def p_prefixe(arbre,liste = []):
    liste.append(arbre.valeur)
    if arbre.gauche:
        p_prefixe(arbre.gauche)
    if arbre.droite:
        p_prefixe(arbre.droite)
    return liste

class File():
    def init(self):
        self.p = []

    def est_vide(self):
        return len(self.p) == 0

    def ajoute(self, val):
        self.p.append(val)

    def supprime(self):
        if len(self.p) != 0:
            return self.p.pop(0)


#______________________________________________________

def p_infixe(arbre,liste2 = []):
    if arbre.gauche:
        p_infixe(arbre.gauche)
    liste2.append(arbre.valeur)

    if arbre.droite:
        p_infixe(arbre.droite)
    return liste2


def p_postfixe(arbre,liste3 = []):
    if arbre.gauche:
        p_postfixe(arbre.gauche)
        
    if arbre.droite:
        p_postfixe(arbre.droite)
    liste3.append(arbre.valeur)
    return liste3


def p_largeur(arbre,liste4 = []):
    file=File()
    file.ajoute(arbre)
    while file.est_vide():
        liste4.append(file.supprime)
        if arbre.gauche:
            p_largeur(arbre.gauche)
        if arbre.droite:
            p_largeur(arbre.droite)
    return liste4




racine = Arbre("A")
racine.insere_gauche("B")
racine.insere_droite("F")
noeud_B=racine.gauche
noeud_B.insere_gauche("C")
noeud_B.insere_droite('D')
noeud_F = racine.droite
noeud_F.insere_gauche('G')
noeud_F.insere_droite('H')
noeud_C = noeud_B.gauche
noeud_C.insere_droite("E")
noeud_G = noeud_F.gauche
noeud_G.insere_gauche('I')
noeud_H = noeud_F.droite
noeud_H.insere_droite('J')
print(p_prefixe(racine))
print(p_infixe(racine))
print(p_postfixe(racine))
print(p_largeur(racine))
