import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Sample: http://py4e-data.dr-chuck.net/comments_42.xml
# Actual: http://py4e-data.dr-chuck.net/comments_1599505.xml

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print('Retrieving', url)

xml = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)
results = tree.findall(".//count")
print(f"Num of count: {len(results)}")

num = 0
for item in results:
    num += int(item.text)

print(f"Sum: {num}")