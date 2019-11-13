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
	'Rio de Janeiro',
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
	place_ids = [
		'508ff478e4b0857f7f609956',
		'53b57a60498ecca74330ec1e',
		'5050a478e4b030bfc6d7e634',
		'4f9ada8ee4b0ec21f43a3652',
		'51afc2a6498e0019436ccd6b',
		'5adaa3efe67742225b5c1a85',
		'5a708b6c92e7a93391ac52e2',
		'565f1d5d498e25a939ca78cc',
		'4fea4ed8e4b073076f9dd6b5',
		'50355976e4b0e092ef2816b5',
		'5962a46db3c9615804173134',
		'50e36e9ce4b0c6dcd8db7c0c',
		'52717f4911d23594e6018342',
		'5776a419498e9c7c7f5be1b1',
		'509d49d5e4b0ab1752c1515c',
		'50f6a3bffe7096f299f3e81e',
		'5a9983a82db4a965fc5a1855',
		'53ffd02d498e1ec054231c30',
		'4f10bd11d5fb04999e39dce5',
		'585daa2c45c3ed1e7db3e921',
		'56675cde498e8e6840609108',
		'50b6b694582f6c88c6687104',
		'50b14f1be4b01d0e2bee99f8',
		'5019aba2e4b08d371bc8e133',
		'585d36d7f595726398dc54a8',
		'50b56d71e4b06863b138f2a6',
		'5730a3fd498e0ee5fcaa7079',
		'54b818a2498ed2e15d559f37',
		'50661a53e4b0679acac08de8',
		'59108a40cab4101c7a07a787',
		'50f6a692fe7096f299f83068',
		'4cbb82814495721e1f0d567a',
		'4fda7d32e4b053a8d41da94e',
		'5362f188498ea8a7b0adf58b',
		'50e43f0ee4b0f6f2e6707088',
		'59b1dd13e2d4aa035dd074ee',
		'52c0b9d6498ea03adb91e080',
		'4d3da8b4557d6dcbcbcb4644',
		'5a46c4e12e26807a2427a1f8',
		'4f8c4e1de4b0af4d50938433',
		'4ef351c046901f708098465d',
		'5bfeb98301bc5a0039ac1471',
		'5090548ee4b019e9fb2299aa',
		'50c2362272da79a2d48683ec',
		'507b54fbe4b01b417b3a013f',
		'50f6e6ce7043b4f4ffa6de5b',
		'4baecfb8f964a5200fda3be3',
		'5205793411d2f8850edddf80',
		'50c1f8e3fe70202788d7af03',
		'577e8db8498ecf23fa22c16b',
		'4c487963786b76b063903ff8',
		'4b9bd070f964a5205e2836e3',
		'52c45f29498eff7ba22aaaa9',
		'4d5198b1dcce224b50b8e31b',
		'4b58798bf964a5207d5928e3',
		'4bba0071935e95215f972790',
		'4e0786e4091afe7701ffe80b',
		'4be8a94d947820a13839b5db',
		'4c20e61d132f0f479e66a796',
		'4c05b7a2761ac9b6c1fd1f74',
		'4ba3b581f964a520025738e3',
		'4be8724e88ed2d7faee1cb1d',
		'4d48a6d29544a093c91020e7',
		'4bcc9a7ab6c49c749b089491',
		'4bc4a3d74cdfc9b685ea9821',
		'4c3a07d4ae2da5939b7d03c6',
		'4c47cf0cd012ef3bfee71ba0',
		'4c3a0f523849c9283f4cc2b1',
		'54a2a4c3498ebc7d8cee9d39',
		'4c84227d88e6199c6665c2d4',
		'4b809d99f964a520348130e3',
		'4bb8b8b298c7ef3bdd523102',
		'5c26a0f26dcf04002d117ae9',
		'4b2cfd98f964a520e7cb24e3',
		'4bcf91bcb221c9b69858d2d0',
		'4be3414721d5a5930ba11811',
		'4c1e926263750f478cf7b967',
		'4e4945e145dd2955e5bbe00f',
		'4ba79d8bf964a520aca239e3',
		'4dcea273183899ddfad71d7c',
		'551e1ece498e16e9027a6077',
		'4c0ea4bd98102d7f61fee306',
		'4c0b04cebbc676b0baf74ad5',
		'4ba26b66f964a5202bf737e3',
		'4c54b9dfa724e21ea611d5f6',
		'5a5a5de7dec1d666f438ecf2',
		'5c261088f00a700039e89791',
		'4b4a33e2f964a520797e26e3',
		'4b529e9af964a520198427e3',
		'4c3270e1ac0ab71396781c1e',
		'4dea8c9545dd3993a88f26fd',
		'4c7d7a6101589521b5f30163',
		'4bc8cfd18b7c9c74b5f938cf',
		'4d7e3a60ebc15481b117dea6',
		'4bf6b84513aed13a1c17eaf7',
		'4db74309bd4191eaa51ee3e4',
		'549ad743498e59f5861e7b01',
		'503ffe83e4b01446aa18818b',
		'4c5adf855c57c9b6f2461e4a',
		'4d148123bb64224b1643ad65',
		'5a8eecbc1108ba6ba7db6ba4',
		'5601dae8498e4f74ba3e31cc',
		'4eef53ae93add02fce44d093',
		'5499f247498ee641a4efb130',
		'56140a09498ef841a0f94482',
		'546b5817498e8875ea325b57',
		'502d662fe4b0bf3e691284ec',
		'4b23dd06f964a520775b24e3',
		'52fe1f17498e9492b7653e5b',
		'51e569f1498e8fc6c8a6811d',
		'53975601498e77d6d162d017',
		'4fb119d16d86b42ae66c909d',
		'56313b20498e97016bad00aa',
		'4d88e018e60c2c0fa41ab63a',
		'5c008ca835d3fc002cfe84ae',
		'4f475cc8e4b0f85d06ca20b2',
		'51d222d4498e0e17a086d407',
		'4fbbce97e4b0c28e72e766cd',
		'4fb7c3c8e4b06a37b6a684bb',
		'59b2bcf031fd145ab68dc581',
		'4b166a32f964a520d3b823e3',
		'59332579cf72a063aa53ffbf',
		'4f7748aae4b08f9be56ed371',
		'59f2dc792bf9a92467813695',
		'4e8f46239a52db7db9ca75ee',
		'59de590661f0706ea6fda3a2',
		'4eb1ceff61af6506d50af137',
		'4cee6098b3662c0f6e6b7430',
		'554d04c9498ed46250bbace1',
		'5b1b0a0d4c9be6002c534fa1',
		'4f71d5aae4b037626fa8d343',
		'5221e197498ee3e390e01a1c',
		'4c0826d6bbc676b0351846d5',
		'51fd7b13498eeb3719e46b54',
		'4d891ee3f607a093b5ffe386',
		'501d787ce4b0f5050c0d755c',
		'4c4101ff520fa593cf05c9ac',
		'538c92b1498e4ac437004900',
		'4e132cc618a84f0f0323800b',
		'4cf95711c6cca35dc46d7f32',
		'4bd3ab77caff9521208cd5f0',
		'4b9d9249f964a52054b436e3',
		'56056630498ee6331dcbd640',
		'4e945d4bc2ee4bf230dc28b6',
		'51085cdae4b0ab948fdff485',
		'4fdf3aa4e4b04e7e2a6274ce',
		'4cf18aac94feb1f73f1118ba',
		'4c768f49c219224bb988a528',
		'4b928cf1f964a5206d0334e3',
		'53eea557498e01d5d1d4a93e',
		'59c9be07a4b51b2d709ccee4',
		'50b13c7fe4b05083c0161e90',
		'4d16a8901356a0933204d782',
		'4c4f657f29fcb7137579f0f1',
		'53a49270498edce8c3141de7',
		'4f037eb09911be1fbc8e77b8',
		'4bf084f821072d7f7c16208b',
		'548b85d0498eb5ef055d5577',
		'4b265c4ef964a5208a7a24e3',
		'4c30d37416adc9289ab7bf9c',
		'54e0b920498ed36be4bb37e9',
		'519aae35498e786c1b666f8e',
		'4c1eb34849139c7403c0a8b7',
		'541345f4498e497019a860cb',
		'4d6d2bd78183a1430637a09f',
		'59ce7b47464d6572f005b77b',
		'4d19f18ccc216ea8a0fb80d3',
		'4e6cdc12b993061ea8ffc6b6',
		'536c0eed498e39fa165cc51a',
		'4f0c42ece4b0614b1491f3f0',
		'4baa4148f964a52010583ae3',
		'564a7dff498e923339cc7485',
		'4d248f33fdfb236a80f77967',
		'4cf3cf90e3b9a093e8ac4b53',
		'4dc2ead4d4c07da16a03d008',
		'4d417f8f915a37045152207f',
		'4b47a262f964a520503826e3',
		'4e13a00cae60fe00dfd88fd1',
		'4bc38dd874a9a593d1b6d4f6',
		'50535a4de4b07f063981977b',
		'4c669965e75ac9281fddf7da',
		'4b2c1110f964a520cdc024e3',
		'546d146d498e83caa542e9d6',
		'5289626211d253e6dba9a4db',
		'5a8a1c5ae679bc79092801c7',
		'573798ac498ed8ebd52d2777',
		'5dab24be8e3e4e0008145733',
		'4e499ccbd164a7c8b69c9b85',
		'4b159229f964a52008af23e3',
		'57fbea10498e66b44dc05c3e',
		'5680513f498e6cbcab81845d',
		'5ab582bb22d49049b157a8ef',
		'4b5b7754f964a520420029e3',
		'56feeb47498e03e9500df5c6',
		'57045c05498e4410fe87e8bc',
		'5c71c7234f0e58002c2dc296',
		'4c8e3fe94e95236a8c3d7aca',
		'4cdc00843f6a8cfac493eeea',
		'5102919fe4b077344ef644e1',
		'4c977ac672dd224b9bd9b491',
		'4fa4886be4b0fd4c3e581411',
		'524cbeeb11d20374f7664678',
		'4b9d71b6f964a52030ad36e3',
		'4b44b171f964a520a0f925e3',
		'5405de94498e9e7e7ef49781',
		'4d2e4abda6df6dcb640ed87a',
		'4ee90c9ad3e31fdba270785d',
		'4b058727f964a520798222e3',
		'4b8e94d0f964a520092a33e3',
		'4d30c8d2f714236ad9e47ba5',
		'4dc864f6e4cd5bc076742b7d',
		'4e580402b3ad0addfaada301',
		'4d8e74c8d4ec8cfa295f7489',
		'4ed91f73d3e346be32c368c2',
		'51804440e4b0ece2aac037c1',
		'4cb5fc08589f236a524d343d',
		'4b2d5ac8f964a520f0d424e3',
		'4ebaf1f329c29ddd428ea7c5',
		'4dcab95fc65bebb82f3f9d46',
		'4beaeb2cf90e9c74f779e3ed',
		'4bd8e3a82e6f0f47cc180908',
		'549ead2c498e29e8a688b487',
		'50e21163e4b01ebc6c92e768',
		'4b40c811f964a52001bb25e3',
		'508b16e5e4b06f6d18a6d126',
		'50f9d4c6e4b084af4e3e6e93',
		'4c4c811d42b4d13aae793180',
		'4dd2f6f6e4cd1b19130e0e8f',
		'4fcc12d8e4b094434fe5cef4',
		'4ca1407579d9b1f7c226be99',
		'4caf6bd55430b713375c3616'
	]
	
# 	for query in queries:
# 		print("Local: " + str(query))

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

# 		# arq = open('saida.json', 'a')
# 		# arq.write(json.dumps(data))
# 		# arq.close()
# 		if data['response']['venues']:
# 			for r in data['response']['venues']:
# 				place_ids.append(r['id'])

# 		# place_ids = set(place_ids)
# 		pp.pprint(place_ids)
# 		pp.pprint("Quantidade de locais: " + str(len(place_ids)))

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
		time.sleep(23)


print("FINISH FOURSQUARE PLACES")
