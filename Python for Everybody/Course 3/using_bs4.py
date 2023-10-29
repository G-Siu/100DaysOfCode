from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if url == "0":
    url = "http://py4e-data.dr-chuck.net/comments_42.html"
elif url == "1":
    url = "http://py4e-data.dr-chuck.net/comments_1915210.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the span tags
tags = soup('span')
num_list = list()
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    num_list.append(int(tag.contents[0]))
print(sum(num_list))
