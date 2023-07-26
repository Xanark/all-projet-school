

class Graphe_or:
    def __init__(self, n):
        self.nombre = n
        self.adj = [n * [False] for _ in range(n)]
        
    def ajouter_arc(self, s1, s2):
        self.adj[s2][s1] = True
        
    def successeurs(self, s):
        a = []
        for elt in self.adj:
            if elt[s] == True:
                a.append(self.adj.index(elt))
        return a
    
    def predecesseurs(self, s):
        a = []
        for i in range(len(self.adj[s])):
            if self.adj[s][i] == True:
                a.append(i)
        return a
    
    def ajouter(self, s):
        self.nombre = s
        for i in range(self.nombre):
            while len(self.adj[i]) != self.nombre:
                self.adj[i].append(False)


def parcours_largeur(graphe, s):
    for i in range():
            



graphe = Graphe_or()
graphe.ajouter_arc("A","B")
graphe.ajouter_arc("A","B")
graphe.ajouter_arc("D", "E")
graphe.ajouter_arc("E","B")
graphe.ajouter_arc("B","C")
graphe.ajouter_arc("C","E")
graphe.ajouter_arc("C","F")
graphe.ajouter_arc("G","C")
print(parcours_largeur(graphe, "A"))