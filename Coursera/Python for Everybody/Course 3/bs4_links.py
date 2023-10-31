from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
repeat = int(input("Enter execution amount: "))
position = int(input("Enter position: "))
if url == "0":
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
elif url == "1":
    url = "http://py4e-data.dr-chuck.net/known_by_Rosina.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

print(url)
tags = soup('a')
for _ in range(repeat):
    links = list()
    for tag in tags:
        links.append(tag.get('href', None))
    url = links[position-1]
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    print(url)
    tags = soup('a')
