# Date: 06 Dec 2023
# Name: G Siu
# colorama module is used
# Fore, Back, Style are functions to change text and background color and style
from colorama import Fore, Back, Style

print(Fore.RED + Back.WHITE + Style.BRIGHT + "This is bold Red text and "
                                             "white background")
print("Text is not normal here !! ")
print(Fore.WHITE + Back.BLACK + Style.NORMAL + "Text is back to normal now !")
