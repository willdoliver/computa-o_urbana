from pymongo import MongoClient
from slugify import slugify
import requests
import time
import json
import re
import folium
import difflib
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import os
 
import pprint
pp = pprint.PrettyPrinter(indent=2)


# https://jtemporal.com/folium/


if __name__ == "__main__":

	client = MongoClient()

	# {'lightblue', 'black', 'darkpurple', 'cadetblue', 'darkblue', 
	# 'beige', 'green', 'purple', 'white', 'lightgray', 'orange', 
	# 'pink', 'lightgreen', 'darkgreen', 'gray', 'darkred', 'red', 'lightred', 'blue'}
	colors = {
	   'Burger King': 'red',
	   'MC Donalds': 'orange',
	   'Starbucks': 'green',
	   'Subway': 'black',
	   'Walmart': 'blue',
	   'Pizza Hut': 'purple', 
	}

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
	   'Burger King',
	   'MC Donalds',
	   'Starbucks',
	   'Subway',
	   'Walmart',
	   'Pizza Hut'
	]


	world = folium.Map(
		location=[0, 0],
		zoom_start = 3
	)

	for local in locations:
		db = client['local']
		slugCity = str(slugify(local)).replace('-', '_')
		database = 'google_' + slugCity
		db = db[database]
		print(local)

		googlePlaces = db.find(
			{},
			{
				"name": 1,
				"rating" : 1,
				"geometry.location": 1
			}
		)

		coords = locations[local].split(',')
		toMap = folium.Map(
			location=[coords[0], coords[1]],
			zoom_start = 10
		)

		for item in googlePlaces:
			try:
				name = difflib.get_close_matches(item["name"], queries, 1, 0.4)[0]
				# print('lat:' +str(item['geometry']['location']['lat']) +' - lng: ' + str(item['geometry']['location']['lng']))
				# print(name + ', color: ' + str(colors[name]))

				folium.Marker(
					location=[item['geometry']['location']['lat'], item['geometry']['location']['lng']],
					icon=folium.Icon(color=colors[name]),
					popup=item['rating']
				).add_to(toMap)

				folium.Marker(
					location=[item['geometry']['location']['lat'], item['geometry']['location']['lng']],
					icon=folium.Icon(color=colors[name]),
					popup=item['rating']
				).add_to(world)
			except:
				# print('deu ruim: ' + str(item["name"]))
				continue
		toMap.save('maps/'+slugCity+'_map.html')
		# exit(0)
	world.save('maps/world_map.html')


