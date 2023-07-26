"""
Leo Dumas
septembre 2022
"""

#exercice 1:



def palindrome_iteratif(mot):
    a=0
    for i in range(len(mot)):
        if ord(mot(i)) == ord(mot(len(mot)-i)):
            a=a+1
    if a== len(mot):
        return True
    else:
        return False
    
print(palindrome_iteratif("radar"),palindrome_iteratif("test"))

def palindrome_recursif(mot,a):
    
    if ord(mot(a)) == ord(mot(len(mot)+a)):
        return True + palindrome_recursif(mot,a+1)
    else: 
        return False

print(palindrome_recursif("radar",0),palindrome_recursif("test",0))

#exercice 2:

def fibonnacci_iteratif(n):
    u0=0
    u1=1
    un=[u0]
    for i in range(n):
        un=+(u0+u1)
        u0=u1
        u1=u0+u1
    print(un)

fibonnacci_iteratif(3)

def fibonnacci_recursif(n):
   if n <= 1:
       return n
   else:
       return(fibonnacci_recursif(n-1) + fibonnacci_recursif(n-2))



print(fibonnacci_recursif(16))