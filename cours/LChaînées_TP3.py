"""
Leo Dumas
septembre 2022
"""

class Liste():

    def __init__(self, val=None, suiv=None):
        self.val=val
        if suiv == None:
            self.suiv=suiv
        else:
            self.suiv=Liste(suiv)
    

    def est_vide(self):
        return self.suiv is None and self.val is None


    def ajoute(self,val1):
        if self.est_vide():
            self.val=val1
        else:
            self.suiv=Liste(self.val,self.suiv)
            self.val=val1

         

    def affiche(self):
        if self.est_vide():
            print("la liste est vide")
        elif self.suiv == None:
            print(self.val)
        else:
            print(self.val)
            return self.suiv.affiche()

   
    

liste=Liste()
liste.affiche()
liste.ajoute(8)
liste.ajoute(-5)
liste.affiche()
liste.ajoute(18)
liste.affiche()