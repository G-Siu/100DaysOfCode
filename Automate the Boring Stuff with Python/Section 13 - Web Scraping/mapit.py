# Use 'run' to search for a place on Google Maps by "mapit some place"
import webbrowser
import pyperclip
import sys

# argument = input("Where would you like to search? Or press enter to "
#                  "paste your clipboard: ").split()
# sys.argv = ["google_maps.py"]
# sys.argv.extend(argument)

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
