__author__ = "Prayas"

#Extracting Data From JSON
import urllib.request, urllib.parse, urllib.error
import json

link = input('Enter location: ')
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

cn = 0
sm = 0
for item in js['comments']:
    cn += 1
    sm += int(item['count'])

print('Count:', cn)
print('Sum:', sm)


#Using The Geo JSON API
import urllib.request, urllib.parse, urllib.error
import json

#Api
api = 'http://py4e-data.dr-chuck.net/geojson?'

#Input data
link = input('Enter location: ')
link = api + urllib.parse.urlencode({'address':link})
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    js = json.loads(html)
except:
    js = None

placeId = js['results'][0]['place_id']
print('Place id', placeId)
