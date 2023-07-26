"""
Leo Dumas
novembre 2022
"""

class Pile():

    def __init__(self, p : list = [None]):
        self.nombres = p
        self.taille = len(p)

    def est_vide(self):
        return self.taille is None

    def empile(self, nbr):
        self.nombres.append(nbr)

    def depile(self):
        a = self.nombres.pop()
        return a

    def affiche(self):
        for i in range(self.taille):
            print(self.nombres[i])


def polonaise(n: str = "1 2 +"):
    n=n.split(' ')
    operation=["*","-","+"]
    pile=Pile()
    pile.empile(int(n[0]))
    pile.empile(int(n[1]))
    
    for i in range(2, len(n)):
        
        try:
            pile.empile(int(n[i]))

        except:
            nb1=int(pile.depile())
            nb2=int(pile.depile())

            if n[i]==operation[0]:
                resultat=nb1 * nb2
            
            elif n[i]==operation[1]:
                resultat=nb1 - nb2
            
            else:
                resultat=nb1 + nb2

            pile.empile(int(resultat))
    
    return pile.depile 

print(polonaise("10 4 -"))
print(polonaise("7 8 * 2 +"))
print(polonaise("1 2 3 * + 4 *"))