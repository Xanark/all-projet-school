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




graphe = Graphe_or(4)
graphe.ajouter_arc(0,1)
graphe.ajouter_arc(0,2)
graphe.ajouter_arc(2,1)
graphe.ajouter_arc(2,3)
graphe.ajouter_arc(3,2)
graphe.ajouter(5)
print(graphe.adj)
print(graphe.successeurs(2))
print(graphe.predecesseurs(1))
