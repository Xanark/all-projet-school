urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:  
        if bulletin in resultat.keys():
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


print(depouille(urne))
print(vainqueur({'A': 3, 'B': 4, 'C': 3}))


#Ex1:

def verifie(tab):
    for i in range(len(tab)-1):
        if tab[i]<=tab[i+1]:
            a=1
        else:
            return False
    return True

"""
print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))
"""

