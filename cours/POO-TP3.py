"""
Leo Dumas
septembre 2022
"""

class Piece :
    nbre_piece=0
   
    def __init__(self, taille=0, nom="anonyme"):
        self.taille = taille
        self.nom=nom
        Piece.nbre_piece+=1

    def get_nom(self):
        return (self.nom)

    def get_surface(self):
        return (self.taille)

    def set_surface(self,val1):
        self.taille=val1


class Appartement :
    nbre_Appartement=0
   
    def __init__(self , nom="anonyme", piece=[]):
        self.nom = nom
        self.piece = piece
        Appartement.nbre_Appartement+=1

    def get_nom(self):
        return (self.nom)
    def get_surface_totale(self):
        for i in range(len(self.piece)):
            a=a+self.piece[i]
        return a
    
    def get_liste_pieces(self):
        return self.piece
    
    def nb_pieces(self):
        return len(self.piece)
    
    #ne fonctione pas :
    def ajouter(self):
        self.piece+=Piece

    


a= Appartement('appt25')
p1 = Piece("chambre", 11.1)
p2 = Piece("sdbToilettes", 7)
p3 = Piece("cuisine", 7)
p4 = Piece("salon", 21.3)
print(p4.get_nom(), p4.get_surface())
p1.set_surface(12.6)
a.ajouter(p1)
a.ajouter(p2)
a.ajouter(p3)
a.ajouter(p4)
print(a.get_nom(), a.get_liste_pieces())

