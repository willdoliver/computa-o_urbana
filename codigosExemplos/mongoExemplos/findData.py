from pymongo import MongoClient

client = MongoClient()
db = client['google_curitiba']

cursor = db.checkins.find({"state":"NY"})

#cursor = db.checkins.find({"user.screen_name": "soldadonofront"})

#cursor = db.checkins.find({"user.followers_count": {"$gt": 5000}})

for document in cursor:
    print(document)
