
from bs4 import BeautifulSoup
from pymongo import MongoClient
from slugify import slugify
import requests
import time
import json
import connection as c

import pprint
pp = pprint.PrettyPrinter(indent=2)

locations = {
    'Curitiba': '-25.432702,-49.268357',
    'São Paulo': '-23.552946,-46.632193',
    'Rio de Janeiro': '-22.912167,-43.206486',
    'Cidade do México': '19.417582,-99.134659',
    'Chicago': '41.878469, -87.667777',
    'New York': '40.757388,-73.982755',
    'Los Angeles': '34.045721,-118.246459',
    'Roma': '41.897421,12.489713',
    'Londres': '51.504603, -0.128073',
    'Berlim': '52.516000,13.405490',
    'Paris': '48.854262, 2.349334',
    'Vancouver': '49.257464, -123.104678',
    'Toronto': '43.679538, -79.415844',
    'Tokyo': '35.683855, 139.763571'
}

queries = [
    'Burger+King',
    'MC+Donalds',
    'Starbucks',
    'Subway',
    'Walmart',
    'Pizza+Hut'
]

url_api = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
key = c.getGoogleKey()
fields = [
    'photos',
    'formatted_address',
    'name',
    'rating',
    'opening_hours',
    'geometry'
]
radius = '50000'

client = MongoClient()

for local in locations:
    print("Cidade: " + str(local))
    database = 'google_' + str(slugify(local)).replace('-', '_')
    db = client['local']
    db = db[database]
    
    for query in queries:
        url_search = url_api+'query='+query+'&key='+key+'&fields='+str(','.join(fields))+'&location='+locations[local]+'&radius='+radius
        # url_temp = url_search
        print("local: " + str(query))

        # aux = 1
        while 1:
            print(url_search)
            time.sleep(4)
            
            req = requests.get(url_search)
            # url_temp = url_search
            page = json.loads(req.content)
            
            # Insere todos os resultados no BD
            
            if 'results' in page:
                db.insert_many(page['results'])
                
            # Validacao para pesquisar nas proximas paginas
            if 'next_page_token' in page:
                # url_temp = url_search
                url_search = url_api+'key='+key+'&pagetoken='+page['next_page_token']
            else:
                break

print("FINISH GOOGLE PLACES")
