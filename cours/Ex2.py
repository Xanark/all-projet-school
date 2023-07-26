"""
Leo Dumas
septembre 2022
"""
import sys
sys.setrecursionlimit(1500)

def somme(n):
    if n == 0:
        return 0
    else:
        return n + somme(n-1)

print(somme(100) , somme(1000) )
