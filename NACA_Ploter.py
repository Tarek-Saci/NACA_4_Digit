import numpy as np
import matplotlib as plt


def generer_tableau_coor(N_point,xx,corde, type_distribution):
    global x_up
    global y_up
    global x_down
    global y_down
    tepaisseur_pourcent = xx/100
    if type_distribution == 'lineaire':
        xc = np.linspace(0 , 1 , N_point)
    elif type_distribution == 'non-uniforme':
        tetha = np.linspace(0 , np.pi , N_point)
        xc = (1/2)*(1-np.cos(tetha))
    yt = 5 * tepaisseur_pourcent * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    x_up = xc * corde
    y_up = yt * corde
    x_down = xc * corde
    y_down = -yt * corde
    return

def pos_epaisseur_max(x_up,y_up):
    i = y_up.index(np.max(y_up)) #position du max de y_up dans le tableau
    pos_epaisseur_max = x_up[i]
    return pos_epaisseur_max

epaisseur_max = lambda y_up : np.max(y_up)

epaisseur_max = np.max(y_up)

def graphique():
    return

xx = int(input('NACA 00XX\n'))
N_point = int(input('Nombre de points\n'))
corde = int(input('corde\n'))
type_distribution = input('type \n')

generer_tableau_coor(N_point, xx,corde,type_distribution)


print(f'x_up = {x_up}')
print(f'y_up = {y_up}')
print(f'x_down = {x_down}')
print(f'y_down = {y_down}')