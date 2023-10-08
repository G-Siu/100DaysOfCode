import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()  # Raises a status if error, does nothing if successful
# print(res.status_code)
# print(len(res.text))
# print(res.text[:500])
with open("RomeoAndJuliet.txt", "wb") as play_file:  # write binary mode,
    # wb, maintains Unicode encoding of text
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
        print(play_file.write(chunk))  # Outputs bytes written to file
