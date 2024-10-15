__author__ = "Prayas"

#Following links in HTML using BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#SSL Certification Error Handle
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collection
link = input('Enter URL: ')
cont = int(input('Enter count: '))
line = int(input('Enter position: '))



print('Retrieving: %s' % link)
for i in range(0, cont):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    cn = 0
    ps = 0
    for tag in tags:
        ps += 1
        if ps == line:
            print('Retrieving: %s' % str(tag.get('href', None)))
            link = str(tag.get('href', None))
            ps = 0
            break


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
