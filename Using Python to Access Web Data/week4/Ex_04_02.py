# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter count: '))
pos = int(input('Enter position: '))
pos = pos - 1

# Retrieve all of the anchor tags
tags = soup('a')
new_url = tags[pos].get('href')
print('Retrieving: ', url)
print('Retrieving: ', new_url)

# Parse through other links in particular position relative to the first name in the list
for i in range(count - 1):
    new_html = urllib.request.urlopen(new_url, context=ctx).read()
    new_soup = BeautifulSoup(new_html, 'html.parser')
    new_tags = new_soup('a')
    new_url = new_tags[pos].get('href')
    print('Retrieving: ', new_url)
    

