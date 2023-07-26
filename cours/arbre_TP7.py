"""
Leo Dumas
decembre 2022
"""


class ARB():
    """Un arbre binaire"""

    def __init__(self, val = None, g = None, d = None):
        self.valeur = val
        self.gauche = g 
        self.droite = d


    def insere(self, val1):
        if val1 < self.valeur:
            if self.gauche is None:
                self.gauche = ARB(val1)

            else:
                self.gauche.insere(val1)
        else:
            if self.droite is None:
                self.droite = ARB(val1)

            else:
                self.droite.insere(val1)

def p_infixe(arbre,liste2 = []):
    if arbre.gauche:
        p_infixe(arbre.gauche)
    liste2.append(arbre.valeur)

    if arbre.droite:
        p_infixe(arbre.droite)
    return liste2

racine= ARB(4)
racine.insere(3)
racine.insere(6)
racine.insere(8)
racine.insere(5)
racine.insere(4)
racine.insere(9)
racine.insere(1)
racine.insere(7)
racine.insere(2)
valeurs = p_infixe(racine)
print(valeurs)
