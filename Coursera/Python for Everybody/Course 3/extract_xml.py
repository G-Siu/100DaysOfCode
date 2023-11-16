import ssl
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter url: ')
    if len(url) < 1:
        break
    elif url == "0":
        url = "http://py4e-data.dr-chuck.net/comments_42.xml"
    elif url == "1":
        url = "http://py4e-data.dr-chuck.net/comments_1915212.xml"
    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print("Retrieved", len(data), "characters")
    print(data.decode())
    tree = ET.fromstring(data)
    counts = tree.findall(".//count")
    print("Count:", len(counts))

    add = list()
    for count in counts:
        add.append(int(count.text))
    print(sum(add))
