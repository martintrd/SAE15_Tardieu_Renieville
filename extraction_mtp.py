## EN DESSOUS LA FONCTION SERA CELLE POUR RECUPERER LES DONNEES

# Nathan Renieville et Tardieu Martin
# 22/01/2023
# Version 1

'''
# Pour faire fonctionner le programme :
    1) - Installer les modules nécessaires avec pip install
    2) - Exécuter le programme

# Ce programme se décompose en trois fonctions.

#La a première fonction nommée creation_dossiers() crée, comme son nom l'indique, tout les dossiers nécessaires pour stocker tout les fichiers que nous récupèreront.


#La deuxième fonction nommée recuperation_info_fixes() vas chercher de nombreux fichiers sur le site https://data.montpellier3m.fr/ tels que :
    #- Les courses de vélo anonymisés
        - Plus précisemment, cette fonction récupère la colonne 4 et 5 qui informe du point de retrait et du point de dépot du vélo, cela permet définir les stations les plus/les moins fréquentés.*
    #- Des informations sur les stations de vélo, comme leur capacité ou leur positions gps
        - Pour pouvoir placés les stations sur une carte, et avoir un pourcentage de remplissage


#La troisième fonction récupère les données en temps réel pour les parkings voiture et vélo:
    #- Pour les voitures, le programme stock les résultats dans un fichier txt au format :
        # Date
        # Nom parking
        # nombre place totale
        # nombre place libre
        # % occupation

    #- Pour les vélos, le programme stock les résultats dans un fichier txt au format :

        # Date de récupération du fichier
        # id_station
        # Nombre vélo disponibles
        # Nombre vélo indisponibles (cassés ou autre)
        # Nombre de docks disponibles (espaces ou l'on peut rendre les vélos)
        # Date du dernier retour de vélo




'''


from requests import get
from lxml import etree
from time import time, sleep            #importations des modules, from x import y pour ne pas importer toute la librairie
from json import dumps, loads
from csv import reader
from os import *
import io

def creation_dossiers():
    dparkings='donnees_parkings'
    dvelosstatiques='donnees_vélos_statiques'
    dvelosmouvements='donnees_vélos_mouvement'
    map='map'
    dveloanonymes='données_velo_anonymes'

    if not path.exists(dparkings):
        mkdir(dparkings)
    if not path.exists(dvelosstatiques):
        mkdir(dvelosstatiques)
    if not path.exists(dvelosmouvements):
        mkdir(dvelosmouvements)
    if not path.exists(dveloanonymes):
        mkdir(dveloanonymes)
    if not path.exists(map):
        mkdir(map)



                                                            #SECTION VELO, DONNEE COURSES #
def recuperation_info_fixes():

    print("\n Téléchargement des courses de vélo anonymisés \n")
    url4 = 'https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_CoursesVelomagg.csv'
    response = get(url4)
    f1=io.open("TAM_MMM_CoursesVelomagg.csv", "w", encoding="utf-8") #J'ai utilisé io.open car open tout seul ne supportait pas le terme encoding, et sans ce terme, la lecture du fichier ne s'effectuait pas
    f1.write(response.text)
    f1.close()

    data= io.open('TAM_MMM_CoursesVelomagg.csv')
    fichierCSV = reader(data, delimiter = ";") #On fait lire le fichier par la fonction reader de la librairies csv, en lui indiquant que le séparateur est : ";"
    liste= []
    for ligne in fichierCSV: # La boucle ci-dessous va chercher les deux cellules que nous voulons (4 et 5). Dans ces cellules elle récupère les 3 premiers caractères, qui correspondent au station id
        if len(ligne)==0 : #Cette ligne permet de ne pas prendre en compte les lignes vides dans le fichier csv
            continue
        else:
            x=ligne[4][0:3]
            y=ligne[5][0:3]
            liste.append(x)
            liste.append(y)
    data.close()
    f1=io.open("données_velo_anonymes/courses_anonymes.txt","w") #l'option "w" permet d'écrire de tout, du texte comme des images ou des audio
    f1.write(str(liste)) #note la liste au format texte
    f1.close()
    remove('TAM_MMM_CoursesVelomagg.csv')





                                                            #SECTION VELO, DONNEE FIXE#
    print("\n Téléchargement des données sur les stations de vélo \n")
    url1="https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json"
    response=get(url1)
    data = response.json()
    data_dumps=dumps(data) #convertit les sous ensemble d'objet en chaine json
    data_dumps=loads(data_dumps)
    for l in range(len(data_dumps["data"]["stations"])):#le fichier json comporte des listes de listes, c'est pour cela que j'ai enchainé plusieurs double crochets pour aller chercher certains élèments
        donnee=str(data_dumps["data"]["stations"][l]["station_id"])+"\n"+str(data_dumps["data"]["stations"][l]["name"])+'\n'+str(data_dumps["data"]["stations"][l]["lat"])+"\n"+str(data_dumps["data"]["stations"][l]["lon"])+"\n"+str(data_dumps["data"]["stations"][l]["capacity"])+'\n'
        f1=io.open("donnees_vélos_statiques/velo_information "+ str(data_dumps["data"]["stations"][l]["station_id"]) +".json","w")
        f1.write(donnee)
        f1.close()






def recuperation_info_tmp_reel(dureetotale,tempsintervalle):

                                                    #SECTION VOITURE, DONNEE VOITURE TEMPS REEL#

    parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRCE','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']  #liste de tout les parkings #parkings erreur : GA109;+GA250;+COME

    drapeau =int(time()) #on vient définir un temps 0 et un drapeau
    temps =int(time())


    while temps < drapeau+dureetotale : #Ce boucle while permet de faire fonctionner le programme pendant x secondes ou x est la dureetotale
        start=int(time())
        for i in parkings :
            temps =int(time())
            url = "https://data.montpellier3m.fr/sites/default/files/ressources/"+ i+".xml"
            response=get(url)

            if response.text != "": #Cette ligne vérifie que le fichier ne soit pas vide
                f1=io.open("donnees_parkings/"+i+".txt","w", encoding='utf8')
                f1.write(response.text)
                f1.close()
                tree = etree.parse("donnees_parkings/"+i+".txt")
                for statut in tree.xpath("Status"):
                    print('Statut du parking :', statut.text)

                for date in tree.xpath("DateTime"):
                    print('Date du téléchargement :', date.text)
                    annee=date.text[0]+date.text[1]+date.text[2]+date.text[3]


                    if int(annee)>=2023 and statut.text =="Open" or statut.text =="Full": #Cette ligne stock le fichier si son statut est "open" ou "full"



                        for nom in tree.xpath("Name"):
                            print('Nom du parking :',nom.text)
                        for nombrepd in tree.xpath("Total"):
                            print('Nombre total de places :',nombrepd.text)
                        for nombrepl in tree.xpath("Free"):
                            print('Nombre de places libres :',nombrepl.text, '\n \n')
                    else :
                        print("ERREUR DANS LE STATUT OU LA DATE DU PARKING:", i, "\n")
                        remove("donnees_parkings/"+i+".txt")
                        continue
                    nombrepd_int=int(nombrepd.text)
                    nombrepl_int=int(nombrepl.text)
                    nombreOccupe=nombrepd_int-nombrepl_int
                    pourcentageOccupation = nombreOccupe*100/nombrepd_int
                    pourcentageOccupation=round(pourcentageOccupation,2)
                    pourcentageOccupation= str(pourcentageOccupation)

                    f1=io.open("donnees_parkings/"+i+"_"+str(temps)+".txt","w", encoding='utf8')
                    f1.write(date.text+ '\n'+ nom.text+'\n'+nombrepd.text+ '\n'+ nombrepl.text +'\n'+pourcentageOccupation+'\n')
                    f1.close()

                    remove("donnees_parkings/"+i+".txt") #Cette ligne supprime le fichier initial (celui avec les balises) pour éviter de prendre de la place inutilement



                                                        #SECTION VELO, DONNEE VELO TEMPS REEL#
        print('\n Téléchargement des données de vélo en temps réels \n')
        temps_v =round(time())
        url2="https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json"
        response=get(url2)
        data = response.json()
        data_dumps=dumps(data) #Cette ligne convertit les sous-ensembles d'objet en chaine json
        data_dumps=loads(data_dumps)
        for l in range(len(data_dumps["data"]["stations"])):
            donnee=str(temps_v)+'\n'+str(data_dumps["data"]["stations"][l]["station_id"])+'\n'+str(data_dumps["data"]["stations"][l]["num_bikes_available"])+'\n'+str(data_dumps["data"]["stations"][l]["num_bikes_disabled"])+'\n'+str(data_dumps["data"]["stations"][l]["num_docks_available"])+'\n'+str(data_dumps["data"]["stations"][l]["last_reported"])+'\n'
            f1=io.open("donnees_vélos_mouvement/velo_status "+ str(data_dumps["data"]["stations"][l]["station_id"]) + "_"+str(temps_v)+".json","a")
            f1.write(donnee)
            f1.close()


        end=int(time()) #Ces lignes permettent de déclencher le téléchargement du premier fichier parkings tous les (attente) secondes. On prend au tout début de la boucle un t0 "start" et ici on prend un t1 "end", on fait la différence, et on retire ce nombre à la variable qu'on à renseigner au démarrage du programme, cela permet de télécharger le premier fichier avec toujours le même écart, même si le débit de la connexion ralenti/accélère. La limite de ces lignes est que, si le temps de téléchargement dépasse le temps d'attente, on aura une attende de -x secondes, et le programme va planter. Nous n'avons rien prévu dans ce cas car il n'arrivera pas. En effet, nous avons décidés de faire un relevé toutes les 10 minutes, et la quantité de fichier à télécharger est inférieure à 1Mo ce qui veut dire qu'il faudrait que la connexion soit inférieure à 1 000 000 / (60*10) = 1 666 = 1.6Ko/s pour poser un problème. Sauf coupure d'internet, c'est impossible.
        tempsexecution=end-start
        attente = tempsintervalle-tempsexecution
        print("Le temps d'attente avant la prochaine prise est de :", attente, "secondes \n")
        sleep(attente)


creation_dossiers()
recuperation_info_fixes()
recuperation_info_tmp_reel(600,60)



