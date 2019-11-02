import flickrapi

api_key = u'xxxxxxxxxx'
api_secret = u'xxxxxxxxxx'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
photos = flickr.photos.search(user_id='73509078@N00', per_page='2')

listPhotos = photos['photos']['photo']
print listPhotos[0]
print listPhotos[1]

#https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
