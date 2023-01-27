#mathDonnee
#Copyright Nathan Renieville et Tardieu Martin
#Version 1.0
#Date d'écriture : 09/01/2023

import os
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

# La fonction ci-dessous calcul la moyenne d'une liste
def calculMoyenne (liste) :
    moyenne = 0
    for i in liste :
        moyenne +=i
    moyenne=moyenne/len(liste)
    return(moyenne)


#La fonction ci-dessous calcul la moyenne puis l'écart type d'une liste :
def ecartType(liste):
    moyenne = 0
    etype=0

    for i in liste :
        moyenne +=i
    moyenne=moyenne/len(liste)

    for j in liste :
        etype += (j-moyenne)**2
    etype /= len(liste)
    etype = sqrt(etype)
    return(etype)


#La fonction ci-dessous crée un graphe avec matplotlib, il faut lui renseigner 5 informations
def courbeGraphe(Lx,Ly,Ly2, Lcmpt, xlabel,ylabel,title):
    plt.plot(Ly, 'b', label='courbe')
    plt.plot(Ly2, 'r', label='limite de saturation')
    plt.xticks(range(len(Ly)), Lx, rotation=10)
    plt.ylim(-10,110)
    plt.legend(loc = 'upper left')
    ax = plt.gca()
    ax.set_xticks(Lcmpt)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


#La fonction ci-dessous permet d'aller récupérer les fichiers nécessaires pour effectuer les analyses des données
def getliste(folder_path):
    for files in os.walk(folder_path):
        for filename in files:
            continue
    return filename


#La fonction ci-dessous permet d'inverser les coordonnées de longitudes et de latitudes si ces coordonnées ne correspondent pas au territoire de la france (sauf dom-tom)
#pour rappel le territoire français se situe entre :
# 51N;5W et 40N;9E, Montpellier est à : 43.37N 3.52E

def reverseCo(fichier_co):
    reverse_co=[]
    for i in fichier_co:
        if i[0]<40 :
            reverse_co.append([i[1],i[0]])


