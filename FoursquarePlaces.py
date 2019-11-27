import time
import json
import requests
import connection as c
from pymongo import MongoClient
from slugify import slugify
from datetime import datetime

import pprint
pp = pprint.PrettyPrinter(indent=2)


locations = [
	# 'Curitiba',
	# 'São Paulo',
	# 'Rio de Janeiro',
	# 'Chicago',
	# 'New York',
	# 'Los Angeles',
	'Roma',
	'Londres',
	'Berlim',
	'Paris',
	'Vancouver',
	'Toronto',
	'Tokyo'
	'Cidade do México',
]

# local, id_category
queries = {
    'Burger+King': '4bf58dd8d48988d16e941735',
    'MC+Donalds': '4bf58dd8d48988d16e941735',
    'Starbucks': '4bf58dd8d48988d1e0931735', 
    'Subway': '4bf58dd8d48988d1c5941735',
    'Walmart': '52f2ab2ebcbc57f1066b8b42',
    'Pizza+Hut': '4bf58dd8d48988d1ca941735'
}

client = MongoClient()
db = client['local']


url_search = 'https://api.foursquare.com/v2/venues/search'
url_venue = 'https://api.foursquare.com/v2/venues/'
params_venue = dict(
  client_id=c.getFoursquareCLIENT_ID(),
  client_secret=c.getFoursquareCLIENT_SECRET(),
  v='20180323'
)


for local in locations:
	print("Cidade: " + str(local))
	place_ids = []
	
	for query in queries:
		print("Local: " + str(query))

		params = dict(
		  client_id=c.getFoursquareCLIENT_ID(),
		  client_secret=c.getFoursquareCLIENT_SECRET(),
		  v='20180323',
		  query=query,
		  categoryId=queries[query],
		  near=local,
		  limit=50
		)

		
		resp = requests.get(url=url_search, params=params)
		data = json.loads(resp.text)

		# arq = open('saida.json', 'a')
		# arq.write(json.dumps(data))
		# arq.close()
		if data['response']['venues']:
			for r in data['response']['venues']:
				place_ids.append(r['id'])

		# place_ids = set(place_ids)
		pp.pprint(place_ids)
		pp.pprint("Quantidade de locais: " + str(len(place_ids)))

	database = 'foursquare_' + str(slugify(local)).replace('-', '_')
	db = client['local']
	db = db[database]

	for id_venue in place_ids:

		cursor = db.find({"response.venue.id":id_venue})
		aux = 0
		for document in cursor:
			aux = 1
		if aux:
			print("Skipped: " + str(id_venue))
			continue

		print(id_venue)
		resp_venue = requests.get(url=url_venue+str(id_venue), params=params_venue)
		data_venue = json.loads(resp_venue.text)

		if data_venue["meta"]["code"] == 429:
			print("Erro 429:" + str(datetime.now()))
			time.sleep(60*60) #1h
			continue
		
		db.insert_one(data_venue)
		time.sleep(34)


print("FINISH FOURSQUARE PLACES")
