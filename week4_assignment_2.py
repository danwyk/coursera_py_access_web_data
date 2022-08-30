# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Sample: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual: http://py4e-data.dr-chuck.net/known_by_Tubagus.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


for num_name in range(0, 7):

    if num_name == 0:
        url = input('Enter - ')
        print("")
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for idx in range(len(tags)):
        if idx == 17:
            # print("Round", num_name)
            # print(tags[idx].get('href', None))
            url = tags[idx].get('href', None)
            # print("-----------------------")
            break

name = re.findall("known_by_(\S+)\.html", str(url))
print(f"Last name is: {name[0]}")
    