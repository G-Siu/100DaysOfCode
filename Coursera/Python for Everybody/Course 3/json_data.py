import json
import ssl
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
        url = "http://py4e-data.dr-chuck.net/comments_42.json"
    elif url == "1":
        url = "http://py4e-data.dr-chuck.net/comments_1915213.json"
    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print("Retrieved", len(data), "characters")
    print(data.decode())

    info = json.loads(data)
    comments = info["comments"]
    print('User count:', len(comments))
    count = list()
    for i in range(len(comments)):
        di = comments[i]
        count.append(di["count"])
    print(sum(count))
