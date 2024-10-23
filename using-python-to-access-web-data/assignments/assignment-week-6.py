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
import urllib.request, urllib.parse, json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

#The following address is different for different students. 
#Choose any one of them by adding a # to the line at the beginning
address = 'Illinois State University Joliet Junior College'#Plus code is 86GGGX9R+5J
address = 'Universidad de la Sabana'#Plus code is 67P7VX68+9P

url = serviceurl + urllib.parse.urlencode({'q': address})

data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)

print(info['features'][0]['properties'] ['plus_code'])
