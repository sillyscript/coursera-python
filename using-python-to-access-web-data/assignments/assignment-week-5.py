__author__ = "Prayas"

import urllib.request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_2089612.xml'
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
counts = tree.findall('.//count')

sum = 0
for count in counts:
    sum += int(count.text)

print('Sum:', sum)