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

    # allPlaces = {}
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

        # ratingPlaces = {}
        ratingPlaces2 = {}
        ratingQtde = {}

        count = 0        
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
                # if name in ratingPlaces:
                #     ratingPlaces[name]['rating'].append(item["rating"])
                #     ratingPlaces[name]['qtde'] += 1
                # else:
                #     ratingPlaces[name] = { 
                #         'rating': [item['rating']],
                #         'qtde': 1
                #     }
            except:
                continue

        for query in queries:
            try:
                ratingPlaces[query]['avg'] = round(sum(ratingPlaces[query]['rating']) / ratingPlaces[query]['qtde'], 2)
                ratingPlaces[query]['min'] = round(min(ratingPlaces[query]['rating']), 2)
                ratingPlaces[query]['max'] = round(max(ratingPlaces[query]['rating']), 2)
                # ratingPlaces[query].pop('rating')
                # ratingPlaces[query].pop('qtde')
            except:
                continue

        # allPlaces[local] = ratingPlaces
        allPlaces2[local] = ratingPlaces2


    # Visualização dos dados
    for local in locations:

        labels = {} 
        data = {}

        labels, data = allPlaces2[local].keys(), allPlaces2[local].values()

        # pp.pprint(allPlaces2[local])
        plt.boxplot(data)
        plt.xticks(range(1, len(labels) + 1), labels, rotation=45)
        plt.title(local)

        plt.xlabel('Locais')
        plt.ylabel('Nota')
        plt.ylim(ymax=5.5)
        plt.ylim(ymin=-0.5)
        plt.subplots_adjust(bottom=0.35)
        
        img_name = 'imagens/'+str(slugify(local)).replace('-', '_')+'Google.png'
        print(img_name)
        plt.savefig(img_name)
        plt.show()


    # Local de acordo com as cidades
    queries = []
    for query in queries:
        
        placesByCity = {}
        labels = {} 
        data = {}

        for local in locations:
            # labels, data = allPlaces2[local][query].keys(), allPlaces2[local][query].values()
            try:
                placesByCity[local] = allPlaces2[local][query]
                # pp.pprint(allPlaces2[local][query])
            except:
                continue

        # pp.pprint(placesByCity)
        # exit(0)
        if query == 'MC Donalds':
            query = 'Mc Donald`s'

        labels, data = placesByCity.keys(), placesByCity.values()

        plt.boxplot(data)
        plt.xticks(range(1, len(labels) + 1), labels, rotation='vertical')
        plt.title(query)
        plt.xlabel('Cidades')
        plt.ylabel('Nota')
        plt.ylim(ymax=5.5)
        plt.ylim(ymin=-0.5)
        plt.subplots_adjust(bottom=0.35)
        
        img_name = 'imagens/'+str(slugify(query)).replace('-', '_')+'Google.png'
        print(img_name)

        plt.savefig(img_name)
        plt.show()

