"""
Leo Dumas
septembre 2022
"""
import random

#Exercice 1 :



class CompteBancaire :
    nbre_compte=0
   
    def __init__(self, nom="anonyme", solde=0):
        self.nom = nom
        self.solde=solde
        CompteBancaire.nbre_compte+=1

    def get_nom(self):
        return (self.nom)
    
    def set_nom(self, val1):
        self.nom=val1
        return(self.nom, self.solde)
    
    def depot(self,valadd1):
        self.solde=self.solde + valadd1
        return (self.nom, self.solde)
    
    def retrait(self,valadd2):
        self.solde=self.solde - valadd2
        return (self.nom, self.solde)
    
    def affiche(self):
        return (self.nom,self.solde)

compte1= CompteBancaire("Duchmol",800)
compte2= CompteBancaire("Trucmuche",200)


print(compte1.get_nom())
#print(compte1.set_nom("nom_changé"))
print(compte1.depot(350))
print(compte1.retrait(200))
print(compte1.affiche())
print("Ce compte appartient à", compte2.get_nom())
print(compte2.depot(500))
print(compte2.affiche())

#Exercice 2 :


class Voiture :
    nbre_voiture=0
   
    def __init__(self, marque="ford", couleur="rouge", pilote="personne", vitesse=0):
        self.marque = marque
        self.couleur=couleur
        self.pilote=pilote
        self.vitesse=vitesse 
        Voiture.nbre_voiture+=1

    def get_marque(self):
        return (self.marque)

    def get_couleur(self):
        return (self.couleur)

    def get_pilote(self):
        return (self.pilote)

    def set_pilote(self, val1):
        self.pilote=val1
        return(self.pilote)

    def accelerer(self,taux,durer):
        if self.pilote != "personne":
            self.vitesse=taux*durer
        else:
            return "pas de pilote"

    def affiche_vitesse(self):
        return (self.vitesse)


a1=Voiture("Peugeot","bleu")
a2=Voiture(couleur="vert")
a3=Voiture("Mercedes")


print(a1.set_pilote("Roméo"))
print(a2.set_pilote("Juliette"))
a2.accelerer(1.8,12)
a3.accelerer(1.9,11)
print(a2.affiche_vitesse())
print("le pilote de la",a2.get_marque(),"est",a2.get_pilote(),",cette voiture est",a2.get_couleur())
print(a3.affiche_vitesse())


#Exercice 3:

class Personnage() :
    nbre_preso=0
   
    def __init__(self, vie):
        self.vie = vie
        Personnage.nbre_preso +=1

    def donne_etat(self):
        return (self.vie)
    def  perd_vie(self):
        val1=random.random()
        if val1>0.5:
            self.vie=self.vie-1
        else:
            self.vie=self.vie-2


bilbo = Personnage(20) 
gollum = Personnage (20) 
while bilbo.donne_etat ( ) > 0 and gollum.donne_etat ( ) > 0 :
    bilbo.perd_vie ( ) 
    gollum.perd_vie ( ) 
    if bilbo.donne_etat ( ) <= 0 and gollum.donne_etat ( ) > 0 :
        msg = " Gollum est vainqueur , Bilbo est mort " 
    elif bilbo.donne_etat ( ) > 0 and gollum.donne_etat ( ) <= 0 :
        msg = " Bilbo est vainqueur , Gollum est mort " 
    else : 
        msg = " Les deux combattants sont morts en même temps " 
print (msg)