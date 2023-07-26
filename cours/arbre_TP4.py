"""
Leo Dumas
novembre 2022
"""

class Arbre:
    """Un arbre binaire"""

    def init(self, val = None, g = None, d = None):
        self.valeur = val
        self.gauche = g 
        self.droite = d

    def insere_droite(self, val):
        """Insere la valeur à droite (nouveau fils droit)"""
        self.droite = Arbre(val, None, self.droite)

    def insere_gauche(self, val):
        """Insere la valeur à gauche (nouveau fils gauche)"""
        self.gauche = Arbre(val, self.gauche, None)

    
def p_sufixe(arbre,liste3 = []):
    if arbre.gauche:
        p_sufixe(arbre.gauche)
    if arbre.droite:
        p_sufixe(arbre.droite)
    liste3.append(arbre.valeur)
    return liste3


    
    


racine = Arbre("A")
racine.insere_gauche("B")
racine.insere_droite("F")
noeud_B = racine.gauche
noeud_B.insere_gauche("C")
noeud_B.insere_droite("D")
noeud_F = racine.droite
noeud_F.insere_gauche("G")
noeud_F.insere_droite("H")
noeud_C = noeud_B.gauche
noeud_C.insere_droite("E")
noeud_G = noeud_F.gauche
noeud_G.insere_gauche("I")
noeud_H = noeud_F.droite
noeud_H.insere_droite("J")
valeurs= p_prefixe(racine)
print(valeurs)
