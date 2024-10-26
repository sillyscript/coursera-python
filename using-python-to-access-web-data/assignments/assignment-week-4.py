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
import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Payton.html' #ans is Sanjay
#url = 'http://py4e-data.dr-chuck.net/known_by_Reis.html' #ans is Archibald
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' #ans is Archibald
##url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' #ans is Ala

count = 7
position = 18

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving:', url)
    url = tags[position - 1].get('href', None)

print('Last name in sequence:', url.split('_')[-1].split('.')[0])
