__author__ = "Prayas"

#Extracting Data From JSON
import urllib.request
import json

url = 'http://py4e-data.dr-chuck.net/comments_2089613.json'
data = urllib.request.urlopen(url).read().decode()

info = json.loads(data)
sum = 0

for item in info['comments']:
    sum += int(item['count'])

print('Sum:', sum)


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
