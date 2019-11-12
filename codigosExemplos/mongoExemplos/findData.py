from pymongo import MongoClient
import pprint
pp = pprint.PrettyPrinter(indent=2)

places = [
	'52a72e3a498eea74a1c51dc0',
  '4bfbfe664b9db713af8ec60b',
  '4bfd8509ee20ef3b00633c5e',
  '4bb4bb06bc82a59333ba3e72',
  '4b9b0c4df964a5209bee35e3',
  '568ae8e8498e1016854bdf7e',
  '5672c771498e9bd379b4e4de',
  '4c3746f593db0f476d701f92',
  '57c9fbb7498e50ae9bc12007',
  '4bb915767421a593c177c240',
  '56c8bb39cd1072488939b2d6',
  '55bc1340498e58c1272c290a',
  '598f33abd7627e661643b7a4',
  '5c02f96f270ee7002c240e54',
  '4cc48be291413704369bc355',
  '55d8f4a8498e5f32db0e4e7b',
  '562ab75d498e46b4256938ec',
  '5c5e319db77c77002cca83cf',
  '5cf80ea09de23b002c010522',
  '597104a7c876c850400a51a4',
  '5ad678d2c0af576cb4b53b69',
  '5c5e305c61e53b002c6f0f00',
  '5aac326e35811b126360b1e5',
  '4df23d8945dd4e26933ba56c',
  '4dc417dbd22dafda2f81fa8c',
  '5722a68e498e6edbbba6aaf4',
  '4cc0d1f16ad3a14336e9d7de',
  '4f4c0303e4b0c132f4a49eb9',
  '4bf40668cad2c9285e689b99',
  '50b8f15de4b077f48c6127d7',
  '4bddb3070ee3a593ae462eb0',
  '5be09a33d552c7002cc4c52a',
  '4cc59f98b2beb1f755c6234c',
  '4c4b03095609c9b6fde88590',
  '4b89e6dff964a520125532e3',
  '4bc92bfe68f976b057fe5c83',
  '4bd8bffa2e6f0f47a16d0808',
  '5be057e91f8ed6002ce04a50',
  '4c5f54c01e5cd13a0c6a9fed',
  '522f911b498e611d60f24752',
  '4bcf168a29d4b713f084a9dc',
  '5caddbf6971317002d8d063e',
  '52a34b1411d202d3815e0216',
  '50aff88be4b0d8a9f031acd4',
  '4efe3ebdf9abd5b38f0d64b9',
  '50e598aee4b063b2718b450d',
  '4eccd0cd93adb82fbc2c429c',
  '4bd9a4290115c9b618fe7780',
  '50d272b2e4b0042ce7ce4358',
  '5c27bd68031320002ce93952',
  '4bcb3108fb84c9b64c471e3e',
  '584720385e56b41f077b4e5b',
  '5da7a9d52ab63a00076f4b6b',
  '50b65899e4b0bc146ba881c5',
  '55625ea6498ef47efd33630c',
  '4c68333c2f6c0f4782e61a7e',
  '50a3f28de4b04c6e7945d221',
  '5224ac6f11d2f67bc291e50e',
  '4bf16ce725afb71349044b6f',
  '528b72b9498ef8e404e38d1a',
  '4b64b32af964a52065c92ae3',
  '4bd6ed2e5631c9b6cf94a630',
  '515afb54e4b0fbffb7fa264b',
  '514751b1e4b0dba1c0bcee67',
  '4c643d7039732d7fb036d4fe',
  '4f884a31e4b055d22edff9a3',
  '4d3e24ae14aa8cfa7b83ba5e',
  '508f09a9e4b014dc938874ea',
  '4f158500e4b045626b2c51f6',
  '52c99b1f498e2304da7f436c',
  '4b870e91f964a5200fae31e3',
  '4bfac4c1bc869521a0fb7a6b',
  '4ba7f824f964a520dcc239e3',
  '4bbe842398f49521456fd163',
  '51942038498e0c624938c36d',
  '507466d6e4b03e9d083a249e',
  '4cc6f633b2beb1f7ee582b4c',
  '4bbca5b58a4fb71382ee3b9d',
  '4bb3c80e715eef3b63d586bb',
  '4bd4647d9854d13aa377ff4d',
  '51dd8257498e3c6e210ef178',
  '5148d49fe4b05523e067e1a5',
  '517c1273498e3d704ebd1be0',
  '5436a8b2498e5eeeb333cf3b',
  '50ff2830e4b07ef68765812c',
  '4f63b9d6e4b0ea77cccf5a7d',
  '53a9d2b6498ecfdaec71fb32',
  '4d2c6e1b915fa093155f1f0a',
  '5399b9fd498eda0a5f8207dc',
  '4cebba7d3608a09000cbae3f',
  '4f294d0ce4b0a2a2c3cd1270',
  '4ef346cfe5fad15c7adb2f4d',
  '4cc0609aa0c4f04d3d6e5a31',
  '5a0c696f8a6f17737ab6a558',
  '5297521e11d27ec8e6e3e105',
  '54e2f2ad498e3c529b37e758',
  '55352d37498e086326d219ac',
  '4ca35f41d7c337044949a062',
  '4bffe628c30a2d7f249e111d',
  '4ca4c1831ee76dcb9e7204de',
  '5228b89511d20e17b40f7eb1',
  '4c0944c4340720a1837d8493',
  '4f835e36e4b062ce209dcacd',
  '4e5ba8dc62e1de72f70df840',
  '4baa8810f964a52018723ae3',
  '59f0b5e208f52105f30ac349',
  '4b92cf0df964a520d91d34e3',
  '4bad3979f964a5203e3b3be3',
  '581d09f2df57f304544dde30',
  '4d07878de350b60cb5f29242',
  '4baff25df964a5208c2d3ce3',
  '4bd9bc07e914a593d5a557fa',
  '5a74e2bbf96b2c278b3ccc4b',
  '5908d425d552c7141f237dad',
  '5db78f1df4e221000895d800',
  '4c407816d691c9b607328b0a',
  '4d9daa24b0fccbff9f803bcf',
  '55de4ce5498eb21f9a7736b0',
  '587174b730ecc65553762afe',
  '50c13e44e4b02a8da22720f3',
  '51ce2952498e2beb95268fb8',
  '4e14fa77483b0d8571cd6ef2',
  '59f27695db1d811d16c56db7',
  '56a2b396498ee6f66102d4cd',
  '4c1120e88c26b7130eb1070b',
  '5ad169bca22db73bb96ddc20',
  '4d2a3411ebacb1f7db820150',
  '58ce7684f840857e7d2dd9ec',
  '586057a39398ab5940a3378c',
  '51dd8653498e4cf0172d7e2e',
  '522206ae11d2cb4e83251e9a',
  '547dc9dc498e321dddf306cf',
  '4cd861415e1b721e17d939d9',
  '5b4e10f9dff8150039bb404b',
  '5d099bdabb8d36002be500fa',
  '520a686711d2aa759ebd5e8d',
  '58742d201e1de562a5625fdc',
  '5234fad7498ed2132370fb8b',
  '55207050498ec57666660c4b',
  '5c94ffa4a35dce002c099ea6',
  '5c20003c1953f3002b57c017',
  '4f838cfae4b0f4019dd3262b',
  '51084507e4b0216ce062caf1',
  '55e0c33d498e77eff09d70b6',
  '4e03d41d1f6e97fbec30bbdb',
  '4bf40197cad2c928d0619b99',
  '4ed16c4702d5feaa1d8425fc',
  '5c268f87610f04002bdeb893',
  '4de98468c65be8091d8ddefb',
  '52646d1f498e476a1bb02a6e',
  '4c22b7339085d13a41dd86cc',
  '54e74ff8498e1e913c47d499',
  '4d7ad76e4755f04d15a8f124',
  '520a68c211d2031f234e4201',
  '5439a508498e918b44d97425',
  '5b0730ad79f6c7002cd1a5a8',
  '520bcf69498e08543206ce0d',
  '514cd79ce4b074491dc032ac',
  '5115d776e4b00949f3dc80db'
]


client = MongoClient()
db = client['local']

# cursor = db.foursquare_curitiba.find({"response.venue.id":"5cf80ea09de23b002c010522"})
cursor = db.foursquare_curitiba.find({"response.venue.id":"5c268f87610f04002bdeb893"})
aux = 0
for document in cursor:
	aux = 1
print(aux)
exit(0)


# print(cursor)
pp.pprint(cursor)

for id_venue in places:
	cursor = db.find({"response.venue.id":id_venue})
	print(cursor)
#cursor = db.checkins.find({"user.screen_name": "soldadonofront"})

#cursor = db.checkins.find({"user.followers_count": {"$gt": 5000}})

