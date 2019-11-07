import json
import requests
import connection as c
from pymongo import MongoClient
from slugify import slugify

import pprint
pp = pprint.PrettyPrinter(indent=2)


locations = [
	# 'Curitiba',
	# 'São Paulo',
	# 'Rio de Janeiro',
	# 'Cidade do México',
	# 'Chicago',
	# 'New York',
	# 'Los Angeles',
	# 'Roma',
	# 'Londres',
	# 'Berlim',
	# 'Paris',
	# 'Vancouver',
	# 'Toronto',
	# 'Tokyo'
]

# local, id_category
queries = {
    # 'Burger+King': '4bf58dd8d48988d16e941735',
    # 'MC+Donalds': '4bf58dd8d48988d16e941735',
    # 'Starbucks': '4bf58dd8d48988d1e0931735', 
    # 'Subway': '4bf58dd8d48988d1c5941735',
    # 'Walmart': '52f2ab2ebcbc57f1066b8b42',
    # 'Pizza+Hut': '4bf58dd8d48988d1ca941735'
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
		print(id_venue)

		resp_venue = requests.get(url=url_venue+str(id_venue), params=params_venue)
		data_venue = json.loads(resp_venue.text)

		# pp.pprint(data_venue)
		# ratings.append(data_venue['response']['venue']['rating']) # Rating value
		db.insert_one(data_venue)


print("FINISH FOURSQUARE PLACES")
