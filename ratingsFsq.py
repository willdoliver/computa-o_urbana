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
        'Chicago',
        'New York',
        'Los Angeles'
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
    
    for local in locations:
        db = client['local']
        database = 'foursquare_' + str(slugify(local)).replace('-', '_')
        db = db[database]
        # print(database)

        fsqPlaces = db.find(
            {},
            {
                "response.venue.name": 1,
                "response.venue.rating" : 1
            }
        )

        aux = []
        ratingPlaces2 = {}
        ratingQtde = {}

        for item in fsqPlaces:

            try:
                name = difflib.get_close_matches(item['response']['venue']['name'], queries, 1, 0.4)[0]
                
                # Versão apenas com local e array de ratings
                if name in ratingPlaces2:
                    ratingPlaces2[name].append(item['response']['venue']['rating']/2)
                else:
                    ratingPlaces2[name] = [] 
                    ratingPlaces2[name].append(item['response']['venue']['rating']/2)
            except:
                continue
        
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
        
        img_name = 'imagens/'+str(slugify(local)).replace('-', '_')+'Fsq.png'
        print(img_name)
        plt.savefig(img_name)
        plt.show()

    # Local de acordo com as cidades
    for query in queries:
        placesByCity = {}
        
        for local in locations:
            try:
                placesByCity[local] = allPlaces2[local][query]
            except:
                continue

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
        
        img_name = 'imagens/'+str(slugify(query)).replace('-', '_')+'Fsq.png'
        print(img_name)
        plt.savefig(img_name)

        plt.show()

