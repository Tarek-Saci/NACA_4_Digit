import numpy as np
import matplotlib.pyplot as plt

#prend en entré toutes les entrées de l'utilisateur pour calculer les tableaux de coordonées
def generer_tableau_coor(N_point,xx,corde, type_distribution):
    #on declare directement le variables en globale pour pouvoir les appeler directement
    global x_up
    global y_up
    global x_down
    global y_down
    epaisseur_pourcent = xx/100
    if type_distribution == 'lineaire':
        xc = np.linspace(0 , 1 , N_point)
    elif type_distribution == 'non-uniforme':
        tetha = np.linspace(0 , np.pi , N_point)
        xc = (1/2)*(1-np.cos(tetha))
    yt = 5 * epaisseur_pourcent * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    x_up = xc * corde
    y_up = yt * corde
    x_down = xc * corde
    y_down = -yt * corde
    return
#calcul de l'epaisseur max
def epaisseur_max (y_up):
    global  epaisseur_max
    epaisseur_max = np.max(y_up)
    return
#calcul de la position de l'epaisseur max le long de la corde
def pos_epaisseur_max(x_up,y_up):
    global pos_epaisseur_max
    max = (np.max(y_up))
    list1 = y_up.tolist()
    i = list1.index(max) #position du max de y_up dans le tableau
    pos_epaisseur_max = x_up[i]
    return
#affichage du graphique
def graphique(x_up,y_up,x_down,y_down):
    plt.plot(x_up, y_up, label='Extrados')
    plt.plot(x_down, y_down, label='Intrados')
    plt.xlabel('Corde [m]')
    plt.ylabel('Épaisseur [m]')
    plt.title(f'Profil NACA 00{xx}')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()
    return

################## les entrées ######################
while True: #boucle pour filtrer l'entrée de l'utilisateur et eviter que le programme crash
    xx = input('Veuillez entrer les deux derniers chiffres du profil NACA 00XX\n')
    if xx.isdigit():
        xx = int(xx)
        break
    else:
        print('veuillez entrer un entier')
    continue
while True: #boucle pour filtrer l'entrée de l'utilisateur et eviter que le programme crash
    N_point = input('Entrez le nombre de points que vous voulez pour tracer la courbe \n')
    if N_point.isdigit():
        N_point = int(N_point)
        break
    else:
        print('veuillez entrer un entier')
    continue

while True: #boucle pour filtrer l'entrée de l'utilisateur et eviter que le programme crash
    corde = input('Veuillez entrer la longeur de corde du profil en mètres \n')
    if corde.isdigit():
        corde = int(corde)
        break
    else:
        print('veuillez entrer un entier')
    continue

while True: #boucle pour filtrer l'entrée de l'utilisateur et eviter que le programme crash
    type_distribution = input('veuillez entrer le type de distribution que vous voulez \'lineaire\' ou \'non-uniforme\' \n')
    if type_distribution == 'lineaire' or type_distribution == 'non-uniforme':
        break
    else:
        print('veuillez entrer (lineaire) ou (non-uniforme)')
    continue
##################################################

#faire tout les calcules
generer_tableau_coor(N_point, xx,corde,type_distribution)
pos_epaisseur_max(x_up,y_up)
epaisseur_max(y_up)

tab_1 = np.vstack((x_up , y_up))
tab_2 = np.vstack((x_down , y_down))

#affichage des tableaux
print(f' [      x_up            y_up     ]  \n{np.transpose(tab_1)}\n\n')
print(f' [     x_down          y_down    ] \n{np.transpose(tab_2)}\n\n')
print(f'epaisseur max : {epaisseur_max} (m)')
print(f'position epaisseur max {pos_epaisseur_max} (m)')
#affichage du graphique
graphique(x_up , y_up , x_down , y_down)