import json
import requests
import connection as c

import pprint
pp = pprint.PrettyPrinter(indent=2)

url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id=c.getFoursquareCLIENT_ID(),
  client_secret=c.getFoursquareCLIENT_SECRET(),
  v='20180323',
  ll='40.7243,-74.0018',
  query='coffee',
  limit=1
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
# print(data)
pp.pprint(data)
