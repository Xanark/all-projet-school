"""
Leo Dumas
septembre 2022
"""

class Pile():

    def __init__(self, val=None, suiv=None):
        self.val=val
        if suiv == None:
            self.suiv=suiv
        else:
            self.suiv=Pile(suiv)
    

    def est_vide(self):
        return self.suiv is None and self.val is None


    def empile(self,val1):
        if self.est_vide():
            self.val=val1
        else:
            self.suiv=Pile(self.val,self.suiv)
            self.val=val1

         


pile=Pile()
pile.empile(8)
pile.empile(12)
print(pile.val)
print(pile.suiv.val)