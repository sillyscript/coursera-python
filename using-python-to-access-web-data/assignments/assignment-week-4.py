__author__ = "Prayas"

#Scraping numbers from HTML using BS4
import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_2091695.html'
#url = 'https://py4e-data.dr-chuck.net/comments_2110014.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
total_sum = 0

for tag in tags:
    total_sum += int(tag.text)

print("Sum:", total_sum)

#sum is 2194 for 2091695
#sum is 2696 for 2110014


#ScrapingHTMLDataWithBeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Get SSL Certification Error handeling
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collect From the Website
link = input('Enter - ')
html = urllib.request.urlopen(link, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')


#Data Scraping
tags = soup('span')
sm = 0
cn = 0
for tag in tags:
    cn += 1
    sm += int(tag.contents[0])

print('Count %d' % cn)
print('Sum %d' % sm)
