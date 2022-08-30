import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter - ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: 
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    place_id = js["results"][0]["place_id"]
    print()
    print("Place_ID:", place_id)
    print("--------------------------------------------")






# {
#     "results": [
#         {
#             "address_components": [
#                 {
#                     "long_name": "Estonia",
#                     "short_name": "EE",
#                     "types": [
#                         "country",
#                         "political"
#                     ]
#                 }
#             ],

#             "formatted_address": "Estonia",

#             "geometry": {
#                 "bounds": {
#                     "northeast": {
#                         "lat": 59.7315,
#                         "lng": 28.2101389
#                     },
#                     "southwest": {
#                         "lat": 57.50931600000001,
#                         "lng": 21.6540999
#                     }
#                 },
#                 "location": {
#                     "lat": 58.595272,
#                     "lng": 25.013607
#                 },
#                 "location_type": "APPROXIMATE",
#                 "viewport": {
#                     "northeast": {
#                         "lat": 59.7315,
#                         "lng": 28.2101389
#                     },
#                     "southwest": {
#                         "lat": 57.50931600000001,
#                         "lng": 21.6540999
#                     }
#                 }
#             },

#             "partial_match": true,

#             "place_id": "ChIJ_UuggpyUkkYRwyW0T7qf6kA",

#             "types": [
#                 "country",
#                 "political"
#             ]
#         }
#     ],
#     "status": "OK"
# }