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
	'São Paulo',
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
		'51bf6c22498e5ddfd68d20fa',
		'4e60f04ad22d509a38f3e64f',
		'54b44181498e268f67f27f22',
		'56ba1a76498ed9b87f127ff3',
		'5da0c18263309a0007528fb7',
		'59cbe04248b04e676a2656d3',
		'5728d633498e47594306747c',
		'4b17e465f964a52054c923e3',
		'51b50155498eb67e4aff5131',
		'4ea88f9a8b8178e107b49415',
		'568ee5d0498e2d4cec749b82',
		'56631e32498e184c5864ee7c',
		'52482e6c498ea0a836194375',
		'51cf27dd498e9bff9be08b1b',
		'556f16e0498e2dcdfdc24882',
		'55ca8f33498e329f7d5d03f3',
		'55495b5f498e8be9d417234f',
		'52c9dd1911d252d54f09c93a',
		'59335f08419a9e4bed93fc45',
		'597fbb7ff1fdaf0cd1b82e0e',
		'5b4a4e559deb7d002c2d06d1',
		'55e5c117498e7d1814a51c3b',
		'5958633dc824ae1df7893d45',
		'57166dae38fa2e4b0be0f731',
		'5221307911d2958235eed90a',
		'5917e90f9ec39941c01961d0',
		'58541fef45c3ed6f71049170',
		'54fb2826498ef41b0165079e',
		'595b96a91de76542cab1151c',
		'4c3517cb452620a1ad46260f',
		'56572f03498ea8fe533bd6b7',
		'5859454e2eb9792b4e928215',
		'4fbfc522e4b099ce167f89bf',
		'53585bdc498ed52bd6369320',
		'4d176fbebb64224b374fc065',
		'519ce6b8498e5df533f12f36',
		'5a02f672a2a6ce635e801dc7',
		'585bdcc80037eb3be7362b50',
		'5a256f1db23dfa2af3cb95c4',
		'52bdcfd311d2d1e4cca99a64',
		'4c23a4c9f1272d7f9fc281c5',
		'550b2dca498e7aa1df1c3b32',
		'5216a1b411d22a75d5a43419',
		'538a7b24498ea2dd8e3466e2',
		'5786769c498ebe3b783d6127',
		'5a490150b04056376860d10e',
		'52fbab76498e4b0d74baad3f',
		'51843f4d498e5a49fb10643d',
		'5339f298498e2c9a16b67b48',
		'4b26699ef964a5202c7b24e3',
		'4c98a5aef419a093ce277188',
		'5cd6ff829cadd9003953701a',
		'4eb4144bf5b94bd85b386edf',
		'4f940e7de4b05b20f10b163e',
		'4cb36c811463a143c967b4a9',
		'4ce500b74303f04d147596b8',
		'4cc20167914137048c20b155',
		'4bfbed82565f76b0912006db',
		'4b201b0af964a520432d24e3',
		'4bc38794920eb7134e961d2c',
		'4bd8c5562e6f0f479c870808',
		'5a5a8b199d6a19650da60bcf',
		'4f9481f1e4b0f08d40ebe665',
		'4c1ce53fb4e62d7f05bbdb93',
		'4bffe5b0f61ea593c1ecea13',
		'51ba63d9498e6d082953ca6a',
		'4b37ba76f964a5201c4525e3',
		'4bb53d26ef159c74be8274f7',
		'4ba521ccf964a52098e138e3',
		'4b12a0f9f964a520878b23e3',
		'4be508192457a593b51bab15',
		'4b508dddf964a5201e2727e3',
		'4b23e8d9f964a520a05c24e3',
		'4bea1107415e20a1fdafe4bb',
		'4b8e8fbef964a520cc2833e3',
		'5527c85e498e7db100277ab2',
		'4b5dee47f964a520727429e3',
		'4b1aa0c5f964a520cded23e3',
		'4c13ed4c7f7f2d7fa700e068',
		'4b5dff8cf964a5204a7829e3',
		'4bd770f309ecb7132ce7467c',
		'4bb4acdd8786ef3b8e7e6533',
		'4c335b9d6f1fef3b8c85ec3d',
		'4eceb2d0f5b9832ad8421849',
		'4bce30b8937ca5930020ae92',
		'4b968d99f964a5202ad434e3',
		'4ffb6b72e4b04858647262ff',
		'50c755cae4b0af5db7fa6e41',
		'4c3ba07c5810a59386feba3c',
		'4b92e432f964a520d02434e3',
		'4beef225f97d952131ed9438',
		'54aaf678498eef83f010110c',
		'4c1a5030b4e62d7f0695d793',
		'4ba142d3f964a5200da737e3',
		'52acf76f498e9cc9b7e1d5e4',
		'4b6dd07cf964a5206c922ce3',
		'4b6d8f3bf964a520997c2ce3',
		'4b92937ef964a520ee0534e3',
		'4bce59c6c564ef3be63aeef0',
		'4bbc7f492d9ea59356a3a0ce',
		'5602dc28498e5def70464fd6',
		'5497e61a498e8683bf27da46',
		'502c15a81648c90f4057be5e',
		'4b081ff6f964a520500423e3',
		'52d9738f498ed22cd0d46d49',
		'504d5bda5262633115d53501',
		'4b1ebef9f964a520e41e24e3',
		'52130a68bce633e66134d64d',
		'50a246338aca18db77fdc64c',
		'4b2907bdf964a520879724e3',
		'56057b50498ecb203f43c9a4',
		'4b1d716ef964a5209d1024e3',
		'553fe1a2498e70d8a136128e',
		'52f523e7498e2847a6de3260',
		'533449c1498e277d365e94e1',
		'55429ea6498ece80e08ba38e',
		'4b50d946f964a5202d3527e3',
		'4f27b764e4b0cec78db6700d',
		'4f82518d0cd6c64c5d2725d2',
		'4dd46b0cc65be32e5f853ead',
		'4f82567e0cd6c64c5d27ad1e',
		'53cef7a3498e4436787bdd28',
		'517e6195498ee8a7d1dc4da2',
		'521de24d11d244c51bfe0bb6',
		'4e6a5a5ba809290267f8ec1a',
		'4b1c3c78f964a520d30424e3',
		'5b02d5835f68b90039957ac5',
		'4b0b0228f964a5207e2b23e3',
		'4fb1194c6d86b42ae66c7fc4',
		'4b0851d2f964a520f30823e3',
		'510c1492e4b0ab88947ac9b0',
		'503c36ebfe70bd66ceb2b8f5',
		'4b169989f964a520bfba23e3',
		'4b088783f964a520c90d23e3',
		'522672ae2fc6aaf1dc4a2a22',
		'55da3ac3498efc34b55080ac',
		'55b12dac498e2180cd687b16',
		'515de63ce4b0ff174bbf02c7',
		'4b265928f964a5206d7a24e3',
		'53108ac8498ec58e16d428ab',
		'503ba59fe4b0b44f29878833',
		'5226724f2fc6aaf1dc49f2f3',
		'4fedeb37e4b0ac0d2ea5d470',
		'4ecd62eff790d070350790f4',
		'5425a315498e59b463b7c258',
		'538527de498e52bf99ebcfdc',
		'5640ca1ccd10bb44cb908f7f',
		'5bf6373de9b9a50025e28923',
		'54c96137498e448626f04080',
		'4b070405f964a52081f522e3',
		'4c41deee3735be9a660c19a4',
		'4c378d3b18e72d7fe5bf16f5',
		'4be067f82aed2d7fd141c86f',
		'4d8b7a2e7139b1f758c8e0d4',
		'4f2d64cce4b0efbc0fca5634',
		'50a11d03e4b0ab1754eb7981',
		'4bb38e2b35f0c9b60a8cbc83',
		'4f0b0747e4b033211c45914b',
		'5065e058e4b0de8be84761b5',
		'50044a52e4b0004dbf5ee0f0',
		'4c5af72a04f9be9a7713f360',
		'4ffdb026e4b023bb62e7229b',
		'5877943875e1372b2061e5ff',
		'4d721703f7c38cfab4aba03d',
		'509d2d12e4b0787347ddb517',
		'4fb28652e4b0294addaa6cdf',
		'5c4b295fb3c961002cd46dbd',
		'528e83c6498e486b2a261cd8',
		'52c20433498ec75771740464',
		'5830929bfc5a5f4d948293cb',
		'4d84a72602eb5481ce6b32f5',
		'4bbc7ddb2d9ea59380a1a0ce',
		'5089558fe4b02705adc3e02c',
		'4cf3bb86c9af6dcb38cca77f',
		'4c349feb3896e21ebcd2eb90',
		'4b89bf49f964a5205a4d32e3',
		'4d8562de81fdb1f7da5f11c0',
		'4d5e75b3e4fe54818cfa679e',
		'5300fff3498eed30c89a7597',
		'4b774089f964a520e58b2ee3',
		'4dba41901e7251d53c78afea',
		'4bbf9cd4920eb71385a4172c',
		'4c79a42f2d3ba1436b138fd0',
		'56de10e1498e48fcbda3e56a',
		'53b820e7498e1b9ab968a18c',
		'520ec73d11d21d65b590fb86',
		'541c57e6498e63d8cb143614',
		'4cc773b93477b60c1223766a',
		'515ca945e4b07a8433355f77',
		'4df8c34bd164d347cc737e90',
		'50957554e4b0baf4e17f01a6',
		'50b1b66a8acab2a5e8a775eb',
		'4ec539960039b25e04636ebd',
		'520c2a3711d20fbc0034446a',
		'4b5346fbf964a5206f9527e3',
		'4c04047939d476b028e430a7',
		'5876942918dc53516f7ab539',
		'4bdc881c2a3a0f471647b3b6',
		'4bf58513e1ef9c7436c3b0ca',
		'4bce3a6eb6c49c747cd79691',
		'4c4ed0d60d90b713e0a5dd78',
		'4ba0b1ecf964a520017837e3',
		'4bcf199bcc8cd13a8155c5cf',
		'4b944ae9f964a520447334e3',
		'4c14108077cea5938c06d060',
		'4b8d648df964a5200ff932e3',
		'4bec36ba9fa3ef3b095280c9',
		'4fad1593e4b0348adb8c50fe',
		'4b927e5af964a52009fe33e3',
		'4c8e3a02d68c6dcb1054faa1',
		'4c0bc94cbbc676b0d7004cd5',
		'4b8c1315f964a52057bc32e3',
		'4bd61b9f29eb9c74579594e1',
		'4c34f499a0ced13a1e0e196e',
		'4bd6c2bd29eb9c74118095e1',
		'4c29d463e19720a1ad03fa58',
		'5732a519498e6ac6438fdf3b',
		'54c02582498e753931537f06',
		'53231891498e183bd059e463',
		'52a39d8511d2141ba004eaa2',
		'54131732498e40e97faa313e',
		'4b256a28f964a5208c7124e3',
		'50c7582fe4b072dfb88708e1',
		'4b2b9908f964a5200db824e3',
		'4bb8f7ae53649c748a8e47fb',
		'52d70002498e7935f09b5eb9',
		'4d0ccb3c3bbaa143a84d38da',
		'4bbf498182a2ef3bad7b2cd2',
		'4b243edbf964a520956424e3',
		'520d085f498e2d9e9c3d9202',
		'4b426d4cf964a520bed325e3',
		'4b991989f964a5203e6135e3',
		'4d0fe2c938bb6ea8d521c1aa',
		'5291a9a7498eb23b2bf75141',
		'51bbc022498e1c3ffda87913',
		'4edbb075be7be28339414efa',
		'504788b7e4b0ea030c44f654',
		'520ba23811d24b6a1cb9f015',
		'53dc7ecb498ec60b0933fc47',
		'52d5b897498e59d44d2b693d',
		'522f491a11d202615e9d76f1',
		'59b85e170531e82b2c350979',
		'52bc6159498e56b452cdb50c',
		'4ebc57b0775bbbe5d6f74462',
		'4c1002bde7d295215fb7d7b0',
		'528d27bc11d23c16a33845bb',
		'5d4a0ca023d6dc00085e829c',
		'5d76d18e49c4700008474b42',
		'4eecf8229a52993fb6b5ea77',
		'4bd08070b221c9b613cad3d0',
		'5370f10b498e0a159499d313',
		'4d264d65b818a35dd815818a',
		'4c818f95d8086dcb8f6e6e52',
		'52988ced498ed1611aa969f3',
		'4d892f9899c2a1cd595876d7',
		'4bc78d6592b376b09af04f3a',
		'4d23817fdaa937046bcdbc81',
		'52961a3811d20e5cbe6adfbe',
		'57b39e29498e63d1b83476fc',
		'522b2e8711d2ff4633e9221e',
		'529739dd11d2c65877e3652c',
		'50ac0212e4b048569b5391b1',
		'4b5b9b53f964a520870a29e3',
		'5025a42de4b0b57d714d0272',
		'5c48cfffc5b11c002c1d7506',
		'566bf871498eb34bc13297ea',
		'52b231b3498e0bd027ffd386',
		'57b789a1498e30ab6bdadd9f',
		'564fa199498e43af36dc8b0d'
	]
	
	# for query in queries:
	# 	print("Local: " + str(query))

	# 	params = dict(
	# 	  client_id=c.getFoursquareCLIENT_ID(),
	# 	  client_secret=c.getFoursquareCLIENT_SECRET(),
	# 	  v='20180323',
	# 	  query=query,
	# 	  categoryId=queries[query],
	# 	  near=local,
	# 	  limit=50
	# 	)

		
	# 	resp = requests.get(url=url_search, params=params)
	# 	data = json.loads(resp.text)

	# 	# arq = open('saida.json', 'a')
	# 	# arq.write(json.dumps(data))
	# 	# arq.close()
	# 	if data['response']['venues']:
	# 		for r in data['response']['venues']:
	# 			place_ids.append(r['id'])

	# 	# place_ids = set(place_ids)
	# 	pp.pprint(place_ids)
	# 	pp.pprint("Quantidade de locais: " + str(len(place_ids)))

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
