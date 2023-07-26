"""
Leo Dumas
fevrier 2023
"""



def recherhe(m,t):
    indices = []
    i = 0
    while i < len(t):
        j = t.find(m, i)
        if j == -1:
            break
        indices.append(j)
        i = j + 1
    return indices


print( recherhe("un","En algorithmique du texte, un algorithme de recherche de sous-chaîne est un type d'algorithme de recherchequi a pour objectif de trouver une chaîne de caractères(le motifM) à l'intérieur d'une autre chaîne (le texte T)."))
