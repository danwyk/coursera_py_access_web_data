# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


# Sample file: http://py4e-data.dr-chuck.net/comments_42.html
# Actual file: http://py4e-data.dr-chuck.net/comments_1599503.html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
spans = soup('span')
num = 0
# print(len(tags) < 1)
for span in spans:
    num += int(span.contents[0])

print('Sum:', num)