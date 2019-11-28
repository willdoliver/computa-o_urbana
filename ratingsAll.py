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
import collections
 
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
    placesGoogle = {}
    placesFsq = {}
    

    ratingPlaces2 = {}
    ratingPlaces3 = {}
    
    for local in locations:
        db = client['local']
        database = 'google_' + str(slugify(local)).replace('-', '_')
        db = db[database]

        googlePlaces = db.find(
            {},
            {
                "name": 1,
                "rating" : 1
            }
        )

        for item in googlePlaces:
            
            try:
                name = difflib.get_close_matches(item["name"], queries, 1, 0.4)[0]
                name = name+' Google'
                if name in ratingPlaces2:
                    ratingPlaces2[name].append(item["rating"])
                else:
                    ratingPlaces2[name] = [] 
                    ratingPlaces2[name].append(item['rating'])
                
            except:
                continue

        # placesGoogle[name] = ratingPlaces2

    for local in locations:
        db = client['local']
        database = 'foursquare_' + str(slugify(local)).replace('-', '_')
        db = db[database]

        fsqPlaces = db.find(
            {},
            {
                "response.venue.name": 1,
                "response.venue.rating" : 1
            }
        )
        
        for item in fsqPlaces:
            
            try:
                name = difflib.get_close_matches(item['response']['venue']['name'], queries, 1, 0.4)[0]
                name = name+' Foursquare'
                # Versão apenas com local e array de ratings
                if name in ratingPlaces3:
                    ratingPlaces3[name].append(item['response']['venue']['rating']/2)
                else:
                    ratingPlaces3[name] = [] 
                    ratingPlaces3[name].append(item['response']['venue']['rating']/2)
            except:
                continue

        # placesFsq[name] = ratingPlaces3

    # print(ratingPlaces2)
    # print(ratingPlaces3)
    # exit(0)
    ratingPlaces2.update(ratingPlaces3)
    ratingPlaces2 = collections.OrderedDict(sorted(ratingPlaces2.items()))
    
    for query in queries:

        labels = {} 
        data = {}

        labels, data = ratingPlaces2.keys(), ratingPlaces2.values()
        # plt.boxplot(data, patch_artist=True)
        box = plt.boxplot(data, patch_artist=True)
        plt.xticks(range(1, len(labels) + 1), labels, rotation=90)
        
        plt.xlabel('Locais')
        plt.ylabel('Nota')
        plt.ylim(ymax=5.5)
        plt.ylim(ymin=-0.5)
        plt.subplots_adjust(bottom=0.38)

        # Adding color in boxes
        colors = []
        for i in data:
            colors.append('blue')
            colors.append('green')

        for patch, color in zip(box['boxes'], colors):
            patch.set_facecolor(color)
        
        img_name = 'imagens/placesAll.png'
        print(img_name)
        plt.savefig(img_name)
        plt.show()
        exit(0)

