"""
Leo Dumas
octobre 2022
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

    def depile(self):
        if self.suiv==None:
            print(self.val)
            self.val=None

        elif self.est_vide():
            self.val=None

        else:
            print(self.val)
            self.val=Pile(self.val,self.suiv)

    def affiche(self):
        if self.est_vide():
            print("la liste est vide")
        elif self.suiv == None:
            print(self.val)
        else:
            print(self.val)
            return self.suiv.affiche()
        
    def __str__(self):
        if self.val is None:
            print(" ")
        elif self.suiv is None:
            print(self.val)
        else:
            print(self.val)
            return "-->",format(str(self.suiv))

pile=Pile()
pile.affiche()
pile.empile(8)
pile.affiche()
pile.empile(-5)
pile.affiche()
pile.empile(18)
pile.affiche()
a= pile.depile()
print(a)
pile.affiche()
a=pile.depile()
print(a)
a=pile.depile()
print(a)
if pile.est_vide():
    print("la liste es vide ")
a=pile.depile()
print(a)
