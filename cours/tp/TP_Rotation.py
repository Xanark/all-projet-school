import PIL.Image as Im




mon_image = "C:\\Users\\lduma\\Desktop\\developement\\dev_py\\tp\\image1.bmp"

#Exercice 1:

image =Im.open(mon_image)
#image.show()
#print("image", image)
largeur , hauteur  = image.size
print(largeur)
print(hauteur)
taille = image.size


#Exercice 2:

matrice_pixels = image.load()
"""
print("pixel rouge" , matrice_pixels[2, 5])
print("pixel gris ", matrice_pixels[73, 5])
print("pixel gris foncer ", matrice_pixels[5, 75])
print("pixel violet ", matrice_pixels[75, 75])
"""

#Exercice 3:
def carré_blanc():
    a = 64
    b = 64 
    for i in range(20):
        for i in range(20):
            matrice_pixels[a,b]=255,255,255
            b=b+1
        a=a+1
        b=64        
    image.save("image_ex3.bmp","BMP")

def permuter(t, taille):
    a=0
    b=0
    haut_gauche = matrice_pixels[0, 0]
    haut_droit = matrice_pixels[taille[0]-1,0]
    bas_gauche = matrice_pixels[0, taille[0]-1]
    bas_droit = matrice_pixels[taille[0]-1, taille[1]-1]

    
    
    for i in range(taille[1]):
        for i in range(taille[0]):
            if a < taille[1]//2:
                if b < taille[0]//2:  
                    
                    matrice_pixels[a,b]=haut_droit
                else:
                    matrice_pixels[a,b]=bas_droit
            else:
                if b < taille[0]//2:  
                    matrice_pixels[a,b]=haut_gauche
                else:
                    matrice_pixels[a,b]=bas_gauche
                    
            b=b+1
        a=a+1
        b=0
        
    image.save("image_ex4.bmp","BMP")

def echange_quart(t, taille):
    a=0
    b=0
    haut_gauche = matrice_pixels[0, 0]
    haut_droit = matrice_pixels[taille[0]-1,0]
    bas_gauche = matrice_pixels[0, taille[0]-1]
    bas_droit = matrice_pixels[taille[0]-1, taille[1]-1]


    for i in range(taille[1]):
        for i in range(taille[0]):
            if a < taille[1]//2:
                if b < taille[0]//2:  
                    
                    matrice_pixels[a,b]=haut_droit
                else:
                    matrice_pixels[a,b]=bas_droit
            else:
                if b < taille[0]//2:  
                    matrice_pixels[a,b]=haut_gauche
                else:
                    matrice_pixels[a,b]=bas_gauche
                    
            b=b+1
        a=a+1
        b=0
  
    a=0
    b=0
   
    for i in range(taille[0]):
        for i in range(taille[0]):
            if a < taille[1]//2:
                if b < taille[0]//2:  
                    matrice_pixels[a,b]=bas_gauche
                else:
                    print("")
            else:
                if b < taille[0]//2:
                    print("")
                else:
                    matrice_pixels[a,b]=haut_droit
            b=b+1
        a=a+1
        b=0
        
    image.save("image_ex4-2.bmp","BMP")

def permuter2(t, taille,ind_c,ind_i):
    a=ind_c
    b=ind_i
    haut_gauche = matrice_pixels[0, 0]
    haut_droit = matrice_pixels[taille[0]-1,0]
    bas_gauche = matrice_pixels[0, taille[0]-1]
    bas_droit = matrice_pixels[taille[0]-1, taille[1]-1]

    
    
    for i in range(2*ind_c):
        for i in range(2*ind_i):
            if a < ind_c*2:
                if b < ind_i*2:  
                    
                    matrice_pixels[a,b]=haut_droit
                else:
                    matrice_pixels[a,b]=bas_droit
            else:
                if b < taille[0]//2:  
                    matrice_pixels[a,b]=haut_gauche
                else:
                    matrice_pixels[a,b]=bas_gauche
                    
            b=b+1
        a=a+1
        b=ind_i
        
    image.save("image_ex5.bmp","BMP")








#print(carré_blanc())
#print(permuter(image, image.size))
#print(echange_quart(image, image.size))
print(permuter2(image, image.size,0,0))