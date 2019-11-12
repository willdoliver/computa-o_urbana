from math import sin, cos, sqrt, atan2, radians
from pymongo import MongoClient
import time
 
import pprint
pp = pprint.PrettyPrinter(indent=2)

def distance(p1, p2):
    # Raio aproximado da terra
    R = 6371.0
 
    lat1 = radians(p1[0])
    lon1 = radians(p1[1])
    lat2 = radians(p2[0])
    lon2 = radians(p2[1])
 
    dlon = lon2 - lon1
    dlat = lat2 - lat1
 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
 
    distance = R * c
 
    return distance


# BK - XV de Novembro - Boca Maldita
# Foursquare
# -25.4452959,-49.2951463
#  Google
# -25.4453461,-49.2953043

if __name__ == "__main__":

    client = MongoClient()
    db = client['local']
    googlePlaces = db.google_curitiba.find(
        {"name":"Burger King"},
        {
            "id": 1,
            "formatted_address" : 1,
            "geometry.location" : 1,
            "rating" : 1
        }
    )

    foursquarePlaces = db.foursquare_curitiba.find(
        {"response.venue.name":"Burger King"},
        {
            "response.venue.id": 1,
            "response.venue.location.address": 1,
            "response.venue.location.lat": 1,
            "response.venue.location.lng": 1,
            "response.venue.rating": 1
        }
    )

    items = {}

    for googlePlace in googlePlaces:
        p1 = (googlePlace['geometry']['location']['lat'], googlePlace['geometry']['location']['lng'])

        distances = []

        for fsqPlace in foursquarePlaces:
            fsqAux = fsqPlace['response']['venue']
            p2 = (fsqAux['location']['lat'], fsqAux['location']['lng'])
            
            d = distance(p1, p2)
            distances.append(d)

            # print(googlePlace["id"] + " --- " + fsqAux["id"] + ' distance: '+ str(d))
            print(str(googlePlace["rating"]) + " --- " + str(fsqAux["rating"]/2) + ' distance: '+ str(d))
        
        distances.sort()
        # pp.pprint(distances)
        # pp.pprint("Menor distancia entre Google:" + googlePlace["id"] + " e Fsq:" + fsqAux["id"]) 
        pp.pprint(str(distances[0]) + " Km")
        exit(0)
