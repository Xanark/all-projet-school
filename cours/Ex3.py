"""
Leo Dumas
septembre 2022
"""



def somme(n):
    if n == 0:
        print(0)
        return 0
    else:
        a= n+somme(n-1)
        print(a)
        return a 
somme(3)
