import json
import requests
import connection as c
from pymongo import MongoClient

import pprint
pp = pprint.PrettyPrinter(indent=2)


locations = [
    'Curitiba'
    # 'São Paulo'
]

queries = {
    'Burger+King': '4bf58dd8d48988d16e941735', # Fast Food Restaurant
    # 'MC+Donalds': '4bf58dd8d48988d16e941735' # Fast Food Restaurant
}
    
###############################################################################

# Search per Burger King Venues in Curitiba for while

# place_ids = []
# url_search = 'https://api.foursquare.com/v2/venues/search'

# for local in locations:
# 	for query in queries:

# 		params = dict(
# 		  client_id=c.getFoursquareCLIENT_ID(),
# 		  client_secret=c.getFoursquareCLIENT_SECRET(),
# 		  v='20180323',
# 		  query=query,
# 		  categoryId=queries[query],
# 		  near=local,
# 		  limit=50
# 		)

# 		resp = requests.get(url=url_search, params=params)
# 		data = json.loads(resp.text)

# 		arq = open('saida.json', 'a')
# 		arq.write(json.dumps(data))
# 		arq.close()

# 		for r in data['response']['venues']:
# 			place_ids.append(r['id'])

# 	place_ids = set(place_ids)
# 	pp.pprint(place_ids)
# 	pp.pprint(len(place_ids))
# 	exit(0)
###############################################################################

place_ids = [  
  '4b9b0c4df964a5209bee35e3',
  '4bb4bb06bc82a59333ba3e72',
  '4bb915767421a593c177c240',
  '4bfbfe664b9db713af8ec60b',
  '4bfd8509ee20ef3b00633c5e',
  '4c3746f593db0f476d701f92',
  '4cc48be291413704369bc355',
  '4dc417dbd22dafda2f81fa8c',
  '4df23d8945dd4e26933ba56c',
  '52a72e3a498eea74a1c51dc0',
  '55bc1340498e58c1272c290a',
  '55d8f4a8498e5f32db0e4e7b',
  '562ab75d498e46b4256938ec',
  '5672c771498e9bd379b4e4de',
  '568ae8e8498e1016854bdf7e',
  '56c8bb39cd1072488939b2d6',
  '5722a68e498e6edbbba6aaf4',
  '57c9fbb7498e50ae9bc12007',
  '597104a7c876c850400a51a4',
  '598f33abd7627e661643b7a4',
  '5aac326e35811b126360b1e5',
  '5ad678d2c0af576cb4b53b69',
  '5c02f96f270ee7002c240e54',
  '5c5e305c61e53b002c6f0f00',
  '5c5e319db77c77002cca83cf',
  '5cf80ea09de23b002c010522'
]


url_venue = 'https://api.foursquare.com/v2/venues/'
params_venue = dict(
  client_id=c.getFoursquareCLIENT_ID(),
  client_secret=c.getFoursquareCLIENT_SECRET(),
  v='20180323'
)

client = MongoClient()
db = client['local']
db = db['foursquare_curitiba']

for id_venue in place_ids:
	print(id_venue)

	resp_venue = requests.get(url=url_venue+str(id_venue), params=params_venue)
	data_venue = json.loads(resp_venue.text)

	pp.pprint(data_venue)
	# ratings.append(data_venue['response']['venue']['rating']) # Rating value
	db.insert_one(data_venue)

	# if id_venue == '4bb4bb06bc82a59333ba3e72':
	# 	exit(0)


print("FINISH FOURSQUARE PLACES")
