db.getCollection("foursquare_curitiba").find({
    }, {
        "response.venue.location.address": 1,
        "response.venue.location.lat": 1,
        "response.venue.location.lng": 1
        }
)

db.getCollection("foursquare_curitiba").find({})

db.getCollection("google_curitiba").find(
    {"id": "810c221acb2b63af7495239854bb23757da22902"}
)
db.getCollection("foursquare_curitiba").find(
    {"response.venue.id": "56c8bb39cd1072488939b2d6"}
)

db.getCollection("foursquare_curitiba").aggregate([
    {"$group" : 
        {
            _id:"response.venue.rating", 
//            avgAmount: { $avg: { $multiply: [ "$price", "$quantity" ] } },
            avgQuantity: { $avg: "$response.venue.rating" }
        }
    }
])

