from urllib import request, parse, error
import json

# Google requires OAuth for maps now
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    url = serviceurl + parse.urlencode({"address": address})
    print("Retrieving", url)
    uh = request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("=== Failure To Retrieve ===")
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lgn)
    location = js["results"][0]["formated_address"]
    print(location)
