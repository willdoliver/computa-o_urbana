from pymongo import MongoClient
from slugify import slugify
import requests
import time
import json
import re
import difflib
import pandas as pd
import matplotlib.pyplot as plt
 
import pprint
pp = pprint.PrettyPrinter(indent=2)



if __name__ == "__main__":

    client = MongoClient()

    locations = [
        'Curitiba',
        'São Paulo',
        'Rio de Janeiro',
        'Cidade do México',
        'Chicago',
        'New York',
        'Los Angeles',
        'Roma',
        'Londres',
        'Berlim',
        'Paris',
        'Vancouver',
        'Toronto',
        'Tokyo'
    ]

    queries = [
        'Burger King',
        'MC Donalds',
        'Starbucks',
        'Subway',
        'Walmart',
        'Pizza Hut'
    ]

    for local in locations:
        db = client['local']
        database = 'google_' + str(slugify(local)).replace('-', '_')
        db = db[database]
        print(local)

        googlePlaces = db.find(
            {},
            {
                "name": 1,
                "rating" : 1
            }
        )

        aux = []
        ratingPlaces = {}
        ratingPlaces2 = {}
        # ratingPlaces = pd.DataFrame(ratingPlaces)

        for item in googlePlaces:
            try:
                name = difflib.get_close_matches(item["name"], queries, 1, 0.4)[0]
                # print(str(name) + ' nota:' +  str(item["rating"]))
                
                if name in ratingPlaces.keys():
                    ratingPlaces[name] += item["rating"]
                else:
                    ratingPlaces[name] = item["rating"]

                if name in ratingPlaces2.keys():
                    ratingPlaces2[name] += 1
                else:
                    ratingPlaces2[name] = 1
            except:
                # print(item["name"])
                continue

            # print(str(item["name"]) + '<>' + str(queries) + ' = ' + str(name))

        # pp.pprint(ratingPlaces2)

        ratings = []
        places = []

        for x in ratingPlaces.keys():
            places.append(x)

        for x in ratingPlaces.values():
            ratings.append(x)
        

        pp.pprint(places)
        pp.pprint(ratings)

        plt.plot(places, ratings)
        plt.title(local)
        plt.xlabel('Local')
        plt.ylabel('Rating')
        plt.show()
        # exit(0)

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
