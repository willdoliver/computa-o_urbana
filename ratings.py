from pymongo import MongoClient
from slugify import slugify
import requests
import time
import json
import re
import difflib
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import os
 
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

    allPlaces = {}
    allPlaces2 = {}
    
    # os.system("sudo service mongodb start")
    
    for local in locations:
        db = client['local']
        database = 'google_' + str(slugify(local)).replace('-', '_')
        db = db[database]
        # print(local)

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
        ratingQtde = {}
        
        for item in googlePlaces:
            try:
                name = difflib.get_close_matches(item["name"], queries, 1, 0.4)[0]
                
                # Versão apenas com local e array de ratings
                if name in ratingPlaces2:
                    ratingPlaces2[name].append(item["rating"])
                else:
                    ratingPlaces2[name] = [] 
                    ratingPlaces2[name].append(item['rating'])
                    
                # Versão com local e valores detalhados
                if name in ratingPlaces:
                    ratingPlaces[name]['rating'].append(item["rating"])
                    ratingPlaces[name]['qtde'] += 1
                else:
                    ratingPlaces[name] = { 
                        'rating': [item['rating']],
                        'qtde': 1
                    }
            except:
                continue

        for query in queries:
            try:
                ratingPlaces[query]['avg'] = round(sum(ratingPlaces[query]['rating']) / ratingPlaces[query]['qtde'], 2)
                # ratingPlaces[query]['min'] = round(min(ratingPlaces[query]['rating']), 2)
                # ratingPlaces[query]['max'] = round(max(ratingPlaces[query]['rating']), 2)
                ratingPlaces[query].pop('rating')
                ratingPlaces[query].pop('qtde')
            except:
                continue

        allPlaces[local] = ratingPlaces
        allPlaces2[local] = ratingPlaces2


    # Visualização dos dados
    for local in locations:
        pp.pprint(allPlaces2[local])

        # https://matplotlib.org/3.1.0/tutorials/introductory/pyplot.html
        # plt.plot([Y], [X])

        plt.plot(allPlaces2[local])
        plt.title(local)
        plt.xlabel('Cidade')
        plt.ylabel('Nota')
        plt.show()
        exit(0)
        
        # pp.pprint(ratingPlaces.values())
        # pp.pprint(ratingPlaces.keys())
        # print(pd.DataFrame(ratingPlaces))

        # fig = plt.figure(1, figsize=(20, 10))
        # ax = fig.add_subplot(111)
        # bp = ax.boxplot(ratingPlaces, patch_artist=True)

        # df = pd.DataFrame(ratingPlaces)
        # df['x'] = pd.Series(ratingPlaces.keys())
        # boxplot = df.boxplot(by='x')
        # exit(0)


        # exit(0)

    pp.pprint(allPlaces)
    
