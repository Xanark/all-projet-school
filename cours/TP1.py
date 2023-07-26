"""
Leo Dumas
septembre 2022
"""
#exercice 1 :

def facto_iter(n):
    for i in range(n-1):
        n *= i+1
    return n

print(facto_iter(7))

def facto_rec(n):

    if n == 1:
        return n
    else :
        return n * facto_rec(n-1)
print(facto_rec(7))


#exercice 2 :

def fonc_puissance(n,x):
    if x == 1:
        return n
    else :
        return n * fonc_puissance(n,x-1)

print(fonc_puissance(7,4))

