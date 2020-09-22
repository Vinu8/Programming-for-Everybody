import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Line 5 to 14 only for reference!

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

address = input('Enter location: ')
print('Retrieving', address)
data = urllib.request.urlopen(address, context=ctx).read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('comments/comment/count')
# OR XPath selector string >>> counts = tree.findall('.//count')
print('Count:', len(counts))

for item in counts:
    sum = sum + int(item.text)
print('Sum:',sum)
