import requests
from datetime import datetime

USERNAME = "garysiudev"
TOKEN = "pakvienwpa0291n8gnq03"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

# today = datetime(year=2020, month=7, day=23)
today = datetime.now()

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Exercises",
    "unit": "completed",
    "type": "int",
    "color": "sora"
}
post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many coding exercises did you complete today? ")
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# For creating username and token
# r = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(r.text)
# For creating graph
# r = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(r.text)
# To post a pixel to graph
# r = requests.post(url=POST_ENDPOINT, json=post_params, headers=headers)
# print(r.text)
# Update existing pixel
# update_endpoint = f"{POST_ENDPOINT}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "1"
# }
# r = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(r.text)
delete_endpoint = f"{POST_ENDPOINT}/{today.strftime('%Y%m%d')}"
r = requests.delete(url=delete_endpoint, headers=headers)
print(r.text)
