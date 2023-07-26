"""
Leo Dumas
Janvier 2023
"""

#Exercice 1:

def dicotomie_iter(t:type = list, v :type = int):
    u=len(t)-1
    u=u//2
    if v not in t:
        return None
    else:
        while(v != t[u]):
            if v < t[u]:
                u = u//2
                
            else:
                u = len(t)//2 + u//2
                
        return u
        

tableau = [i for i in range(100) if i % 3 !=0]
indice1 = dicotomie_iter(tableau, 15)
indice2 = dicotomie_iter(tableau, 98)
print(indice1, indice2)

#Exercice 2:
def dicotomie_recursive(t,v,g,d):
    u = g+d
    u = u//2
    if v not in t:
        return None

    else:
        if v == t[u]:
            return u

        elif v < t[u]: 
            return dicotomie_recursive(t,v,g,u+1)   

        else:
            return dicotomie_recursive(t,v,u+1,d)


tableau = [i for i in range(100) if i % 3 !=0]
indice1 = dicotomie_recursive(tableau, 15, 0, len(tableau)-1)
indice2 = dicotomie_recursive(tableau, 98, 0, len(tableau)-1)
print(indice1, indice2) 
