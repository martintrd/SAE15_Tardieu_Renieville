## Cette fonction est là pour afficher toutes les cartes

# Nathan Renieville et Tardieu Martin
# 19/01/2023
# Version 1

from ressource_fonction import *
from requests import get
from json import dumps, loads
import folium


ressource_extra= [
{"nom":'Saint Jean le Sec',"Ylat":'43.5751462',"Xlong":"3.8307894"},
{"nom":'Sablassou',"Ylat":'43.6334885',"Xlong":"3.9222722"},
{"nom":'Circé Odysseum',"Ylat":'43.604865',"Xlong":"3.9181444"},
{"nom":'Gare',"Ylat":'43.6036306',"Xlong":"3.8789449"},
{"nom":'Foch Préfecture',"Ylat":'43.6106755',"Xlong":"3.8762608"},
{"nom":'Viccarello',"Ylat":'43.6326978',"Xlong":"3.8984116"},
{"nom":'Gaumont EST-OUEST',"Ylat":'43.60392',"Xlong":"3.9143625"},
]


def dico_ressources():
    ressource={"Antigone":"FR_MTP_ANTI","Comédie":"","Corum":"FR_MTP_CORU","Europa":"FR_MTP_EURO","Foch_Prefecture":"FR_MTP_FOCH","Gambetta":"FR_MTP_GAMB","Gare":"FR_MTP_GARE","Triangle":"FR_MTP_TRIA","Arc de Triomphe":"FR_MTP_ARCT","Pitot":"FR_MTP_PITO","Circe-Odysseum":"FR_MTP_CIRC","Sabines":"FR_MTP_SABI","Garcia Lorca":"FR_MTP_GARC","Notre-Dame-de-Sablassou":"FR_MTP_SABL","Mosson":"FR_MTP_MOSS","Saint-Jean-le-Sec":"FR_STJ_SJLC","Euromedecin":"FR_MTP_MEDC","Occitanie":"FR_MTP_OCCI","Viccarello":"FR_CAS_VICA","Gaumont EST":"","Gaumont OUEST":"","Charles de Gaulle":"FR_CAS_CDGA","Arceaux":"FR_MTP_ARCE","Polygone":"FR_MTP_POLY"}
    return ressource

ressource={"Antigone":"FR_MTP_ANTI","Comédie":"","Corum":"FR_MTP_CORU","Europa":"FR_MTP_EURO","Foch Préfecture":"FR_MTP_FOCH","Gambetta":"FR_MTP_GAMB","Gare":"FR_MTP_GARE","Triangle":"FR_MTP_TRIA","Arc de Triomphe":"FR_MTP_ARCT","Pitot":"FR_MTP_PITO","Circé Odysseum":"FR_MTP_CIRC","Sabines":"FR_MTP_SABI","Garcia Lorca":"FR_MTP_GARC","Notre Dame de Sablassou":"FR_MTP_SABL","Mosson":"FR_MTP_MOSS","Saint-Jean-le-Sec":"FR_STJ_SJLC","Euromédecine":"FR_MTP_MEDC","Occitanie":"FR_MTP_OCCI","Vicarello":"FR_CAS_VICA","Gaumont EST":"","Gaumont OUEST":"","Charles de Gaulle":"FR_CAS_CDGA","Arceaux":"FR_MTP_ARCE","Polygone":"FR_MTP_POLY"}

url2 = "https://data.montpellier3m.fr/sites/default/files/ressources/VilleMTP_MTP_ParkingOuv.geojson"
response = get(url2)
data = response.json()




# def rendu_cartes_tram():
#                     #ajoute les tram sur la map#
#     carte = folium.Map(location=[43.608792, 3.875865], zoom_start=13)
#     url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_LigneTram.json"
#     data_tram = folium.GeoJson(url, style_function=fonction_couleur).add_to(carte)
#
#
#     carte.save('map/CarteTram.html')
#
#
#
#
#
# def rendu_cartes_tout():
#                     #ajoute les tram sur la map#
#     carte = folium.Map(location=[43.608792, 3.875865], zoom_start=12)
#     url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_LigneTram.json"
#     data_tram = folium.GeoJson(url, style_function=fonction_couleur).add_to(carte)
#
#                     #ajoute les parkings depuis un fichier opendata
#     url2 = "https://data.montpellier3m.fr/sites/default/files/ressources/VilleMTP_MTP_ParkingOuv.geojson"
#     response = get(url2)
#     data = response.json()
#
#     for i in data["features"]:
#         popup_info ="Parking:", i["properties"]["nom"],  "Type: ", i["properties"]["domanialit"]
#
#         if i["properties"]["nom"] in ressource :
#             folium.Marker(
#             location=[i["properties"]["Ylat"],i["properties"]["Xlong"]],
#             popup=popup_info,
#             icon=folium.Icon(color="blue", icon="info-sign"),).add_to(carte)
#
#         else :
#             if i["properties"]["Ylat"] == None:
#                 continue
#             else:
#                 folium.Marker(
#                 location=[i["properties"]["Ylat"],i["properties"]["Xlong"]],
#                 popup=popup_info,
#                 icon=folium.Icon(color="darkblue", icon="info-sign"),).add_to(carte)
#
#                 # ajout des parkings ne figurant pas sur le fichier open data
#     for j in ressource_extra:
#         popup_info2 ="Parking:", j["nom"]
#         folium.Marker(
#         location=[j["Ylat"],j["Xlong"]],
#         popup=popup_info2,
#         icon=folium.Icon(color="blue", icon="info-sign"),).add_to(carte)
#
#     for i in range(len(getliste('donnees_vélos_statiques'))):
#         with open("donnees_vélos_statiques/"+getliste('donnees_vélos_statiques')[i],'r') as fichier:
#             fichier=fichier.readlines()
#             position=[fichier[0][0:-1],fichier[1][0:-1],fichier[2][0:-1],fichier[3][0:-1]]
#
#         popup_info2 ="Parking vélo:", position[1]
#         folium.Marker(
#         location=[position[2],position[3]],
#         popup=popup_info2,
#         icon=folium.Icon(color="green", icon="info-sign"),).add_to(carte)
#
#
#
#
#     carte.save('map/CarteTout.html')
#
#
#
# def rendu_cartes_chq_parking():
#
#
#                     #ajoute les parkings depuis un fichier opendata
#     url2 = "https://data.montpellier3m.fr/sites/default/files/ressources/VilleMTP_MTP_ParkingOuv.geojson"
#     response = get(url2)
#     data = response.json()
#     url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_LigneTram.json"
#     for i in data["features"]:
#
#         popup_info ="Parking:", i["properties"]["nom"],  "Type: ", i["properties"]["domanialit"]
#         if i["properties"]["nom"] in ressource :
#
#             carte = folium.Map(location=[i["properties"]["Ylat"],i["properties"]["Xlong"]], zoom_start=14)
#
#             data_tram = folium.GeoJson(url, style_function=fonction_couleur).add_to(carte)
#             folium.Marker(
#             location=[i["properties"]["Ylat"],i["properties"]["Xlong"]],
#             popup=popup_info,
#             icon=folium.Icon(color="blue", icon="info-sign"),).add_to(carte)
#             carte.save(f'map/Carte{i["properties"]["nom"]}.html')
#
#         else :
#             if i["properties"]["Ylat"] == None:
#                 continue
#             else:
#                 folium.Marker(
#                 location=[i["properties"]["Ylat"],i["properties"]["Xlong"]],
#                 popup=popup_info,
#                 icon=folium.Icon(color="darkblue", icon="info-sign"),).add_to(carte)
#
#
#
#
#
# def fonction_couleur(info): #choix couleur pour les lignes de tram
#     couleur = 'blue'
#     if info['properties']['nom'] == 'LIGNE 2':
#         couleur = 'orange'
#     elif info['properties']['nom'] == 'LIGNE 3':
#         couleur = 'black'
#     elif info['properties']['nom'] == 'LIGNE 4':
#         couleur = 'yellow'
#     return {'color': couleur}

#
# def map_velo_extension():
#     carte = folium.Map(location=[43.608792, 3.875865], zoom_start=12)
#     url3='https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_ReseauExpressVeloREV.json'
#     data_velo = folium.GeoJson(url3, style_function=lambda x: {'color':'darkviolet'}).add_to(carte) #ici on se sert de lambda de x car c'est une fonction qui ne necessite pas d'être réutilisée/ inutile, je ne l'ai pas fait pour fonction_couleur qui comportait 4 couleurs différentes
#                     #ajoute les parkings depuis un fichier opendata
#     url2 = "https://data.montpellier3m.fr/sites/default/files/ressources/VilleMTP_MTP_ParkingOuv.geojson"
#     response = get(url2)
#     data = response.json()
#
#     for i in data["features"]:
#         popup_info ="Parking:", i["properties"]["nom"],  "Type: ", i["properties"]["domanialit"]
#
#         if i["properties"]["nom"] in ressource :
#             folium.Marker(
#             location=[i["properties"]["Ylat"],i["properties"]["Xlong"]],
#             popup=popup_info,
#             icon=folium.Icon(color="blue", icon="info-sign"),).add_to(carte)
#
#         else :
#             if i["properties"]["Ylat"] == None:
#                 continue
#             else:
#                 folium.Marker(
#                 location=[i["properties"]["Ylat"],i["properties"]["Xlong"]],
#                 popup=popup_info,
#                 icon=folium.Icon(color="darkblue", icon="info-sign"),).add_to(carte)
#
#                 # ajout des parkings ne figurant pas sur le fichier open data
#     for j in ressource_extra:
#         popup_info2 ="Parking:", j["nom"]
#         folium.Marker(
#         location=[j["Ylat"],j["Xlong"]],
#         popup=popup_info2,
#         icon=folium.Icon(color="blue", icon="info-sign"),).add_to(carte)
#
#     for i in range(len(getliste('donnees_vélos_statiques'))):
#         with open("donnees_vélos_statiques/"+getliste('donnees_vélos_statiques')[i],'r') as fichier:
#             fichier=fichier.readlines()
#             position=[fichier[0][0:-1],fichier[1][0:-1],fichier[2][0:-1],fichier[3][0:-1]]
#             print(position)
#
#         popup_info2 ="Parking vélo:", position[1]
#         folium.Marker(
#         location=[position[2],position[3]],
#         popup=popup_info2,
#         icon=folium.Icon(color="green", icon="info-sign"),).add_to(carte)
#
#     carte.save('map/CarteVeloExtension.html')
#

# def rendu_chq_parkings_velo():
#     for i in range(len(getliste('donnees_vélos_statiques'))):
#         with open("donnees_vélos_statiques/"+getliste('donnees_vélos_statiques')[i],'r') as fichier:
#             fichier=fichier.readlines()
#             position=[fichier[0][0:-1],fichier[1][0:-1],fichier[2][0:-1],fichier[3][0:-1]]
#
#             carte = folium.Map(location=[position[2],position[3]], zoom_start=15)
#             popup_info2 ="Parking vélo:", position[1]
#             folium.Marker(
#             location=[position[2],position[3]],
#             popup=popup_info2,
#             icon=folium.Icon(color="green", icon="info-sign"),).add_to(carte)
#
#             url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_LigneTram.json"
#             data_tram = folium.GeoJson(url, style_function=fonction_couleur).add_to(carte)
#             url2 = "https://data.montpellier3m.fr/sites/default/files/ressources/VilleMTP_MTP_ParkingOuv.geojson"
#             response = get(url2)
#             data = response.json()
#             for i in data["features"]:
#                 popup_info ="Parking:", i["properties"]["nom"],  "Type: ", i["properties"]["domanialit"]
#                 if i["properties"]["nom"] in ressource :
#                     folium.Marker(
#                     location=[i["properties"]["Ylat"],i["properties"]["Xlong"]],
#                     popup=popup_info,
#                     icon=folium.Icon(color="blue", icon="info-sign"),).add_to(carte)
#                 else :
#                     if i["properties"]["Ylat"] == None:
#                         continue
#                     else:
#                         folium.Marker(
#                         location=[i["properties"]["Ylat"],i["properties"]["Xlong"]],
#                         popup=popup_info,
#                         icon=folium.Icon(color="darkblue", icon="info-sign"),).add_to(carte)
#
#                         # ajout des parkings ne figurant pas sur le fichier open data
#             for j in ressource_extra:
#                 popup_info2 ="Parking:", j["nom"]
#                 folium.Marker(
#                 location=[j["Ylat"],j["Xlong"]],
#                 popup=popup_info2,
#                 icon=folium.Icon(color="blue", icon="info-sign"),).add_to(carte)
#
#
#
#
#                 carte.save('map/CarteVelo'+position[1]+'.html')





# rendu_chq_parkings_velo()
# print("oui1")
# rendu_cartes_tram()
# print("oui3")
# rendu_cartes_tout()
# print("oui5")
# rendu_cartes_chq_parking()
# print("oui6")
# map_velo_extension()



#   cd C:\\Users\\natha\\Desktop\\IUT nathan\\1ère année R&T\\cours\\Saé 15 - Données\\A.projet\\Programme pour rendu final
