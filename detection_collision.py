import numpy as np
#import dictionnaire

# nb_particule = 10 
# x = np.ones(nb_particule) #vecteurs positions en x de chaque particule
# y = np.ones(nb_particule) #vecteurs positions en y de chaque particule
# r = [] #vecteurs des rayons de chaque particules



def collision_inter(x,y,nb_particule,r):
    
    """
    x: Vecteur des positions en x
    y: vecteur des positions en y
    r: Vecteur des rayons de chaque particule

    La fonction retourne la matrice de collision NxN entre chacune des particules. 
    Si un element est 0: Il n'y a pas de collisions
    Si un element est 1: Il y a collision entre les particules
    """


    colli_inter = np.zeros((nb_particule,nb_particule)) # matrice de detection de collision

    for i in range(0,nb_particule+1):
        for j in range(0,nb_particule+1):
            R = np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            if R < r[i]*r[j]:
                colli_inter[i,j] = 1
    
    
    return colli_inter



def collision_mur(x,y,nb_particule,r,box_xsize,box_ysize):

    """
    x: Vecteur des positions en x
    y: vecteur des positions en y
    r: Vecteur des rayons de chaque particule
    box_xsize: Longueur de la boite en x
    box_ysize: Longueur de la boite en y

    La fonction reotourne la matrice de collision avec le mur (4xN)
    1er ligne: Collision avec le mur de gauche
    2e ligne: Collision avec le mur de droite
    3e ligne: Collision avec le mur du bas
    4e ligne: Collision avec le mur du haut
    """

    x_mur = [0,box_xsize]
    y_mur = [0,box_ysize]
    colli_mur = np.zeros((4,nb_particule)) 

    for i in range(0,nb_particule+1):
        if x_mur[1]>x[i]:
            colli_mur[1,i] = 2
        if x[i]-r[i]<x_mur[1] and x_mur[1]<x[i]:
            colli_mur[1,i] = 1
        if x_mur[2]<x[i]:
            colli_mur[2,i] = 2
        if x[i]<x_mur[2] and x_mur[2]<x[i]+r[i]:
            colli_mur[2,i] = 1
        if y_mur[1]>y[i]:
            colli_mur[3,i] = 2
        if y[i]-r[i]<y_mur[1] and y_mur[1]<y[i]:
            colli_mur[3,i] = 1
        if y_mur[2]<y[i]:
            colli_mur[4,i] = 2
        if y[i]<y_mur[2] and y_mur[2]<y[i]+r[i]:
            colli_mur[4,i] = 1
    
   
    return colli_mur