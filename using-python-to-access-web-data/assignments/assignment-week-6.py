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

address = 'Illinois State University Joliet Junior College'
url = serviceurl + urllib.parse.urlencode({'q': address})

data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)

#This line is not correct,
#run it in terminal print the info then parse through that info to get the plus code properly. 
#As far as I remember it also had a list so put accordingly. 
plus_code = info['plus_code']['global_code']

print('Plus code:', plus_code)
