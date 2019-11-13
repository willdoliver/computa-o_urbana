db.getCollection("foursquare_curitiba").find({
    }, {
        "response.venue.location.address": 1,
        "response.venue.location.lat": 1,
        "response.venue.location.lng": 1
        }
)

db.getCollection("foursquare_curitiba").find({})

db.getCollection("google_curitiba").find(
                {"name": /.*Pizza Hut.*/},
                {
                    "name": 1,
                    "rating" : 1
                });
                
                
db.getCollection("foursquare_curitiba").find(
    {"response.venue.id": "56c8bb39cd1072488939b2d6"}
)


db.business.aggregate([
    {"$group" : {_id:"$state", count:{$sum:1}}}
])

db.getCollection("yelp_review").find({})


db.getCollection("foursquare_curitiba").aggregate([
    {"name": "Burger King"},
    {"$group" : 
        {
            _id:"response.venue.rating", 
//            avgAmount: { $avg: { $multiply: [ "$price", "$quantity" ] } },
            avgQuantity: { $avg: "$response.venue.rating" }
        }
    }
])

