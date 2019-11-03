
from bs4 import BeautifulSoup
from pymongo import MongoClient
from slugify import slugify
import requests
import time
import json
import time
import connection as c

import pprint
pp = pprint.PrettyPrinter(indent=2)

locations = {
    'Curitiba': '-25.432702,-49.268357',
    'São Paulo': '-23.552946,-46.632193',
    # 'Rio de Janeiro': 'zzz,xxx',
    # 'Chicago': 'zzz,xxx',
    # 'New York': 'zzz,xxx',
    # 'Los Angeles': 'zzz,xxx',
    'Las vegas': '36.167157,-115.144949',
    # 'Barcelona': 'zzz,xxx',
    # 'Madrid': 'zzz,xxx',
    # 'Roma': 'zzz,xxx',
    # 'Veneza': 'zzz,xxx',
    # 'Tokyo': 'zzz,xxx',
    # 'Londres': 'zzz,xxx',
    # 'Berlim': 'zzz,xxx',
    # 'Moscou': 'zzz,xxx',
    # 'Paris': 'zzz,xxx',
    # 'Buenos Aires': 'zzz,xxx',
    # 'Quebec': 'zzz,xxx',
    # 'Vancouver': 'zzz,xxx'
}

queries = [
    'Burger+King',
    'MC+Donalds',
    # 'Starbucks',
    # 'Subway',
    # 'Walmart',
    # 'Pizza+Hut',
    # 'Forever+21',
    # 'MAC',
    # 'GAP',
    # 'The+North+Face',
    # 'Nike',
    # 'Adidas',
    # 'Aeropostale',
    # 'Guess',
    # 'Hollister',
    # 'Tommy+Hilfiger'
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

        aux = 1
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

print("FINISH PLACES")
