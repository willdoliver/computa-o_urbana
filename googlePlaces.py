
import requests
import time
import json
from bs4 import BeautifulSoup

locations = {
    'Curitiba': '-25.432702,-49.268357',
    'São Paulo': '-23.552946,-46.632193',
    'Rio_de Janeiro': 'zzz,xxx',
    'Chicago': 'zzz,xxx',
    'New York': 'zzz,xxx',
    'Los Angeles': 'zzz,xxx',
    'Barcelona': 'zzz,xxx',
    'Madrid': 'zzz,xxx',
    'Roma': 'zzz,xxx',
    'Veneza': 'zzz,xxx',
    'Tokyo': 'zzz,xxx',
    'Londres': 'zzz,xxx',
    'Berlim': 'zzz,xxx',
    'Moscou': 'zzz,xxx',
    'Paris': 'zzz,xxx',
    'Buenos Aires': 'zzz,xxx',
    'Quebec': 'zzz,xxx',
    'Vancouver': 'zzz,xxx'
}

queries = [
    'Burger+King',
    'MC+Donalds',
    'Starbucks',
    'Subway',
    'Walmart',
    'Pizza+Hut',
    'Forever+21',
    'MAC',
    'GAP',
    'The+North+Face',
    'Nike',
    'Adidas',
    'Aeropostale',
    'Guess',
    'Hollister',
    'Tommy+Hilfiger'
]

sep = '&'

url_api = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
query = 'Burger King'
key = 'AIzaSyAfCTfMi7XctJldjCxi7ZquvblPf0bJEt4'
fields = [
    'photos',
    'formatted_address',
    'name',
    'rating',
    'opening_hours',
    'geometry'
]
radius = '50000'


for local in locations:
    
    #print(url_search)
    req = requests.get(url_api+
        'query='+queries[0]+'&'+
        'key='+key+'&'+
        'fields='+str(','.join(fields))+'&'+
        'location='+locations[local]+'&'+
        'radius='+radius
    )

    page = json.loads(req.content)
    print(page['results'][0])
    
    exit(0)
