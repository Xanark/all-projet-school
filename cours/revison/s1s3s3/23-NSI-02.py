def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1

print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positif([-2]))

def indices_maxi(tab):
    max = 0
    liste=[]
    for i in range(len(tab)):
        if tab[i]> max:
            max =tab[i]
    for i in range(len(tab)):
        if max ==tab[i]:
            liste.append(i)
    list_final=(max, liste)
    
    return list_final




#print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) )
#print(indices_maxi([7]))