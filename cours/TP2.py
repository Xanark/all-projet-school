"""
Leo Dumas
septembre 2022
"""

#exercice 1:

from operator import index


def boucle(i,k):
    print(i)
    if i == k:
        return k
    else:
        return i + boucle(i+1,k)

boucle(0,3)

#exercice 2:

def appartient(v,tab,i):

    if v == tab[i]:
        return True 
    
    elif i+1 == len(tab):
        return False
    else:
        return appartient(v,tab,i+1)

print(appartient(4,[1,7,9],1))
print(appartient(4,[1,8,4,7,9],2))

#exercice 3:


def syracuse(n):
    if n == 1:
        return int(n)
    else:
        print(int(n))
        if n % 2 ==0 :
            return syracuse(n/2) 
        else:
            return syracuse(3*n+1)

print(syracuse(2))

#exercice 4:

#def serie(n,a,b):
   

#print(serie())

#exercice 5:

def minimum(tab : list):
    if len(tab) == 0:
        return tab[0]
    else:
        if tab[0] > tab[1]:
            return minimum(tab.pop(1))
        else:
            return minimum(tab.pop(0))

print(minimum([8,9,4,6,4,3,1]))