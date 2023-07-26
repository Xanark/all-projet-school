"""
Leo Dumas
Mars 2023
"""

def occurences(chaine):
    dico={}
    for lettre in chaine:
        dico[lettre] = 1
    for lettre in chaine:
        for clef in dico.keys():
            if lettre == clef:
                dico[clef] +=1
    for clef in dico.keys():
            dico[clef] -=1   

    return dico



print(occurences("grammaire"))

