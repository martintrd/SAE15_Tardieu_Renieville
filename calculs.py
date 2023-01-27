import os
import codecs
from bs4 import BeautifulSoup as BS
from ressource_fonction import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from rendu_visuel_des_cartes import *
from datetime import datetime, timedelta
from time import time


##Tri des fichiers afin de traiter les données dans l'ordre
folder_path_parkings = "donnees_parkings"
folder_path_vélos_statiques = "donnees_vélos_statiques"
folder_path_vélos_mouvement = "donnees_vélos_mouvement"
folder_path_parkings = "donnees_parkings"
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRCE','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']  #liste de tout les parkings #parkings erreur : GA109;+GA250;+COME




Lparking=getliste(folder_path_parkings)
Lvélos_statiques=getliste(folder_path_vélos_statiques)
Lvélos_mouvement=getliste(folder_path_vélos_mouvement)
L_déjà_fait=[]
Ldfall=[]

def tri_par_nom(liste):
	L2=[]
	L_déjà_fait=[]
	button = 1
	for x in range(len(liste)):
		nom=''
		if liste==Lparking :
			for y in range(11):
				nom=nom+liste[x][y]
		elif liste==Lvélos_statiques :
			for y in range(15):
				nom=nom+liste[x][y]
		elif liste==Lvélos_mouvement :
			for y in range(19):
				nom=nom+liste[x][y]
		for df in L_déjà_fait:
			if df != nom :
				button = 1
			else :
				button = 0
				break
		if button == 1 :
			L=[]
			for z in range(len(liste)):
				nom2=''
				if liste==Lparking :
					for y in range(11):
						nom2=nom2+liste[z][y]
				elif liste==Lvélos_statiques :
					for y in range(15):
						nom2=nom2+liste[z][y]
				elif liste==Lvélos_mouvement :
					for y in range(19):
						nom2=nom2+liste[z][y]
				if nom == nom2 :
					L.append(liste[z])
			L2.append(L)
			L_déjà_fait.append(nom)
	Ldfall.append(L_déjà_fait)
	return L2

tri_parking=tri_par_nom(Lparking)
tri_vélos_statiques=tri_par_nom(Lvélos_statiques)
tri_vélos_mouvement=tri_par_nom(Lvélos_mouvement)




##Traitement de l'occupation des parkings
liste_pourcentage=[]
for a in tri_parking:
	for txt in a:
		with open('donnees_parkings/'+txt, "r") as f:
			pourcentage=''
			data = f.readlines()[4]
			for i in range(len(data)):
				if data[i]=='/n' :
					pourcentage+=0
				else :
					pourcentage+=data[i]
		liste_pourcentage.append(pourcentage)

dico_parkings={}
cmpt=0
for nbr in range(len(tri_parking)) :
	for nbr2 in range(len(tri_parking[nbr])) :
		dico_parkings[f'{tri_parking[nbr][nbr2]}']=liste_pourcentage[cmpt]
		cmpt+=1


d_ressources=dico_ressources()

tri_d_ressources=[]
for i in range(len(Ldfall[0])):
	for clef, valeur in d_ressources.items():
		if valeur == Ldfall[0][i]:
			tri_d_ressources.append(clef)

#Cette liste (L4) permet de stocker par parking les différents pourcentages d'occupations à 10 minutes d'intervalle
L4=[]
for x in range(len(tri_parking)):
	L3=[]
	for y in range(len(tri_parking[x])):
		L3.append(float(dico_parkings[tri_parking[x][y]]))
	L4.append(L3)


LMoyenne_chq_parking=[]
for j in range(len(L4)):
	LMoyenne_chq_parking.append(round(calculMoyenne(L4[j]),2))


LMoyenne_tous_parkings=round(calculMoyenne(LMoyenne_chq_parking),2)
print('Les parkings renseignés dans l\'open data de Montpellier durant la période du jeudi 19/01/2023 au vendredi 20/01/2023 ont été comblés à :', LMoyenne_tous_parkings, '% en moyenne')




Lécart_type_chq_parking=[]
for j in range(len(L4)):
	Lécart_type_chq_parking.append(round(ecartType(L4[j]),2))

Lécart_type_tous_parkings=round(ecartType(Lécart_type_chq_parking),2)
print('Les parkings renseignés dans l\'open data de Montpellier durant la période du jeudi 19/01/2023 au vendredi 20/01/2023 ont un écart type de :', Lécart_type_tous_parkings, 'en moyenne')

Lcmptall=[]
Lxall=[]
date=""
for b in range(len(L4)):
	Lx=[]
	cmpt=0
	Lcmpt=[]
	button=1
	for c in range(len(L4[b])):
		with open('donnees_parkings/'+tri_parking[b][c], "r") as f:
			x=''
			x2=''
			data = f.readlines()[0]
			for i in range(10):
				x+=data[i]
			for i in range(11,13):
				x2+=data[i]
		if (x2 == '06' or x2 == '12' or x2 == '18' or x2 == '00') and button == 0 :
			Lx.append(None)
		elif (x2 == '06' or x2 == '12' or x2 == '18' or x2 == '00') and button == 1:
			j=''
			for i in range(19):
				j+=data[i]
			Lx.append(j)
			Lcmpt.append(cmpt)
			date=x
			button = 0
		else :
			Lx.append(None)
			button = 1
		cmpt+=1
	Lxall.append(Lx)
	Lcmptall.append(Lcmpt)





Ly=[]
for i in range(len(L4[0])):
	Ly.append(90)

for y in range(len(L4)):
	courbeGraphe(Lxall[y],L4[y],Ly,Lcmptall[y],'temps','Pourcentage d\'occupation', f'Pourcentage d\'occupation du parking {tri_d_ressources[y]} en fonction du temps')
	plt.savefig(f'imgs/parking_{tri_d_ressources[y]}.png')
	plt.clf()# Définir la limite de valeur

fmodele=open(f'parkings/modèle_parking.html','r', encoding="utf8")
fall=fmodele.read()
for park in range(len(tri_d_ressources)):
	fpark=open(f'parkings/{tri_d_ressources[park]}.html','w', encoding="utf8")
	fpark.write(fall)
	fpark.close()






##Traitement de l'occupation des points vélos
liste_dispos_velos=[]
for a in tri_vélos_mouvement:
	for txt in a :
		with open("donnees_vélos_mouvement/"+txt, "r") as f:
			dispos=''
			data = f.readlines()[2]
			for i in range(2):
				if data[i]=='\n':
					dispos+=''
				else:
					dispos+=data[i]
			liste_dispos_velos.append(dispos)



liste_indispos_velos=[]
for a in tri_vélos_mouvement:
	for txt in a :
		with open("donnees_vélos_mouvement/"+txt, "r") as f:
			indispos=''
			data = f.readlines()[4]
			for i in range(len(data)):
				if data[i]=='\n':
					indispos+=''
				else:
					indispos+=data[i]
			liste_indispos_velos.append(indispos)


liste_pourcentage_velos=[]
for i in range(len(liste_dispos_velos)):
	if liste_dispos_velos[i] != '0' and liste_indispos_velos != '0' :
		pourcentage_velos=round(int(liste_dispos_velos[i])/(int(liste_indispos_velos[i])+int(liste_dispos_velos[i]))*100,2)
		liste_pourcentage_velos.append(pourcentage_velos)
	else :
		liste_pourcentage_velos.append(0)



Lposition=[]
for i in range(len(getliste('donnees_vélos_statiques'))):
	position=[]
	with open("donnees_vélos_statiques/"+getliste('donnees_vélos_statiques')[i],'r',encoding='utf8') as fichier:
		fichier=fichier.readlines()
		position=[fichier[0][0:-1],fichier[1][0:-1],fichier[2][0:-1],fichier[3][0:-1]]
	Lposition.append(position)




L6=[]
cmpt=0
for x in range(len(tri_vélos_mouvement)):
	L5=[]
	for y in range(len(tri_vélos_mouvement[x])):
		L5.append(liste_pourcentage_velos[cmpt])
		cmpt+=1
	L6.append(L5)


LMoyenne_chq_velos=[]
for j in range(len(L6)):
	LMoyenne_chq_velos.append(round(calculMoyenne(L6[j]),2))


LMoyenne_tous_velos=round(calculMoyenne(LMoyenne_chq_velos),2)
print('Les velos renseignés dans l\'open data de Montpellier durant la période du jeudi 19/01/2023 au vendredi 20/01/2023 ont été disponibles à :', LMoyenne_tous_velos, '% en moyenne')




Lécart_type_chq_velos=[]
for j in range(len(L6)):
	Lécart_type_chq_velos.append(round(ecartType(L6[j]),2))

Lécart_type_tous_velos=round(ecartType(Lécart_type_chq_velos),2)
print('Les vélos renseignés dans l\'open data de Montpellier durant la période du jeudi 19/01/2023 au vendredi 20/01/2023 ont un écart type de :', Lécart_type_tous_velos, 'en moyenne')



Lcmptall=[]
Lxall=[]
date=""
date2=""
epoch = datetime(1970, 1, 1)
for b in range(len(L6)):
	Lx=[]
	cmpt=0
	Lcmpt=[]
	button=1
	for c in range(len(L6[b])):
		with open('donnees_vélos_mouvement/'+tri_vélos_mouvement[b][c], "r") as f:
			x=''
			x2=''
			data = f.readlines()[0]
			for i in range(len(data)):
				x+=data[i]
			x=int(x)
			date2 = epoch + timedelta(seconds=x)
			x=date2.strftime("%d/%m/%Y")
		if (date2.strftime("%H") == "06" or date2.strftime("%H") == "12" or date2.strftime("%H") == "18" or date2.strftime("%H") == "00") and button == 0:
			Lx.append(None)
		elif (date2.strftime("%H") == "06" or date2.strftime("%H") == "12" or date2.strftime("%H") == "18" or date2.strftime("%H") == "00") and button == 1:
			Lx.append(date2.strftime("%d/%m/%Y %H:%M:%S"))
			Lcmpt.append(cmpt)
			date=x
			button = 0
		else :
			Lx.append(None)
			button = 1
		cmpt+=1
	Lxall.append(Lx)
	Lcmptall.append(Lcmpt)


Ly=[]
for i in range(len(L6[0])):
	Ly.append(80)

ressources_velos=Lvelos()

for y in range(len(L6)):
	courbeGraphe(Lxall[y],L6[y],Ly, Lcmptall[y], 'temps','Pourcentage d\'occupation', f'Pourcentage d\'occupation de l\'emplacement {ressources_velos[y]} en fonction du temps')
	plt.savefig(f'imgs/velos_{ressources_velos[y]}.png')
	plt.clf()# Définir la limite de valeur

fmodele=open(f'velos/modèle_velos.html','r', encoding="utf8")
fall=fmodele.read()
for park in range(len(ressources_velos)):
	fpark=open(f'velos/{ressources_velos[park]}.html','w', encoding="utf8")
	fpark.write(fall)
	fpark.close()




## Changement du index.html avec les données de Open Data
with open('index.html','r',encoding='utf8') as f1:
	stats_all=f1.read()

	soup=BS(stats_all, features="lxml")

	for p in soup.find_all('h1', attrs={'id' : '1'}):
		p.string=str(LMoyenne_tous_parkings)+' %'

	for p in soup.find_all('h1', attrs={'id' : '2'}):
		p.string=str(Lécart_type_tous_parkings)

	for p in soup.find_all('h1', attrs={'id' : '3'}):
		p.string=str(LMoyenne_tous_velos)+' %'

	for p in soup.find_all('h1', attrs={'id' : '4'}):
		p.string=str(Lécart_type_tous_velos)

with open('index.html','w',encoding='utf8') as f1:
	f1.write(str(soup))






## Changement du d_parkings.html avec les données de Open Data
for i in range(len(tri_d_ressources)):
	with open('d_parkings.html','r',encoding='utf8') as f1:
		fallparkings=f1.read()

		soup=BS(fallparkings, features="lxml")

		for p in soup.findAll('a', attrs={'id' : str(i+1)}):
			p["href"] = 'parkings/'+tri_d_ressources[i]+'.html'
			p["class"] = 'parkings'

		for p in soup.findAll('div', attrs={'id' : str(i+1)}):
			p["class"] = 'parkings2'
			p["style"] = 'background-image: url("imgs/Carte'+tri_d_ressources[i]+'.png");'

		for p in soup.findAll('h1', attrs={'id' : str(i+1)}):
			p.string = tri_d_ressources[i]

	with open('d_parkings.html','w',encoding='utf8') as f1:
		f1.write(str(soup))

## Changement du d_velos.html avec les données de Open Data
for i in range(len(ressources_velos)):
	with open('d_velos.html','r',encoding='utf8') as f1:
		fallvelos=f1.read()

		soup=BS(fallvelos, features="lxml")

		for p in soup.findAll('div', attrs={'id' : str(i+1)}):
			p["class"] = 'parkings2'
			p["style"] = 'background-image: url("imgs/CarteVelos'+ressources_velos[i]+'.png");'

		for p in soup.findAll('a', attrs={'id' : str(i+1)}):
			p["href"] = 'velos/'+ressources_velos[i]+'.html'
			p["class"] = 'parkings'

		for p in soup.findAll('h1', attrs={'id' : str(i+1)}):
			p.string = ressources_velos[i]

	with open('d_velos.html','w',encoding='utf8') as f1:
		f1.write(str(soup))

## Changement des html des parkings avec les données de Open Data
for i in range(len(tri_d_ressources)):
	with open(f'parkings/{tri_d_ressources[i]}.html','r',encoding='utf8') as f1:
		parking=f1.read()
		soup=BS(parking, features="lxml")

		for p in soup.find_all('img', attrs={'id' : 'imgfig'}):
			p["src"] = '../imgs/parking_'+tri_d_ressources[i]+'.png'

		for p in soup.find_all('h1', attrs={'id' : '1'}):
			p.string=str(LMoyenne_chq_parking[i])+' %'

		for p in soup.find_all('h1', attrs={'id' : '2'}):
			p.string=str(Lécart_type_chq_parking[i])
	with open(f'parkings/{tri_d_ressources[i]}.html','w',encoding='utf8') as f1:
		f1.write(str(soup))

## Changement des html des velos avec les données de Open Data
for i in range(len(ressources_velos)):
	with open(f'velos/{ressources_velos[i]}.html','r',encoding='utf8') as f1:
		velos=f1.read()
		soup=BS(velos, features="lxml")

		for p in soup.find_all('img', attrs={'id' : 'imgfig'}):
			p["src"] = '../imgs/velos_'+ressources_velos[i]+'.png'

		for p in soup.find_all('h1', attrs={'id' : '1'}):
			p.string=str(LMoyenne_chq_velos[i])+' %'

		for p in soup.find_all('h1', attrs={'id' : '2'}):
			p.string=str(Lécart_type_chq_velos[i])
	with open(f'velos/{ressources_velos[i]}.html','w',encoding='utf8') as f1:
		f1.write(str(soup))


