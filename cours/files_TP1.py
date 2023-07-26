"""
Leo Dumas
octobre 2022
"""


#Exercice 1:

class File():

    def __init__(self, f:list=[]):
        self.f=f
    

    def est_vide(self):
        return self.f is None 

    def ajoute(self,val):
        self.f.append(val)

    def suprime(self):
        print(self.f[0])
        self.f.pop(0)

    def affiche(self):
        print(self.f)


"""   
file=File()
file.affiche()
file.ajoute(8)
file.affiche()
file.ajoute(-5)
file.affiche()
file.ajoute(18)
file.affiche()
a = file.suprime()
print(a)
file.affiche()
a = file.suprime()
print(a)
a = file.suprime()
print(a)
if file.est_vide():
    print("la liste es vide ")
a = file.suprime()
print(a)
"""

#Exercice 2:

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
        if self.suiv==None():
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

pile1=Pile()
pile2=Pile()

class File():

    def __init__(self, entre=pile1, sorti=pile2):
        self.entre=entre
        self.sorti=sorti

    def est_vide(self):
        return self.entre is None and  self.sorti is None

    def ajoute(self,val):
        self.entre.empile(val)
    
    def suprime(self):
        if self.est_vide():
            return None
        else:
            for i in range(len(file)):
                self.sorti.empile(file(i))
            self.sorti.depile()

            
file=File()
for i in range(5):
    file.ajoute(i)
print(file.entre)
for i in range(6):
    a = file.suprime()
    print(a)