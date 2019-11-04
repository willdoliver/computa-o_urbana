import json
import requests
import connection as c

import pprint
pp = pprint.PrettyPrinter(indent=2)

url_search = 'https://api.foursquare.com/v2/venues/search'
params = dict(
  client_id=c.getFoursquareCLIENT_ID(),
  client_secret=c.getFoursquareCLIENT_SECRET(),
  v='20180323',
  # ll='40.7243,-74.0018',
  query='Burger+King',
  near='Curitiba, PR',
  limit=5
)

# resp = requests.get(url=url_search, params=params)
# data = json.loads(resp.text)

# place_ids = []

# for r in data['response']['venues']:
# 	place_ids.append(r['id'])

# pp.pprint(place_ids)

place_ids = [ '52a72e3a498eea74a1c51dc0',
  '4bfbfe664b9db713af8ec60b',
  '4b9b0c4df964a5209bee35e3',
  '4bfd8509ee20ef3b00633c5e',
  '4bb4bb06bc82a59333ba3e72']


url_venue = 'https://api.foursquare.com/v2/venues/'
params_venue = dict(
  client_id=c.getFoursquareCLIENT_ID(),
  client_secret=c.getFoursquareCLIENT_SECRET(),
)

ratings = []

for id_venue in place_ids:
	resp_venue = requests.get(url=url_venue+str(id_venue), params=params_venue)
	data_venue = json.loads(resp_venue.text)
	pp.pprint(data_venue['response']['venue']['rating'])
	ratings.append(data_venue['response']['venue']['rating'])
	# exit(0)

pp.pprint(ratings)