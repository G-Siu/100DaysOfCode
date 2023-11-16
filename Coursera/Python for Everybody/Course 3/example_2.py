import ssl
from urllib import request, parse, error

from bs4 import BeautifulSoup

# Ignore SSL certificate errors (in case SSL doesn't exist on webpage)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of hte anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
