import re


# ------------------------Regex groups and pipe character-------------------------
phoneNumRegex = re.compile(r"\(\d\d\d\) \d\d\d-\d\d\d\d")  # \(\) finds the parenthesis
mo = phoneNumRegex.search("My number is (415) 555-4242")
# print(mo.group())
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
ba = batRegex.search("Batmobile lost a wheel")
# print(ba.group())
# print(ba.group(0))
# print(ba.group(1))
# -----------------------------------Repetition-----------------------------------
batRegex = re.compile(r"Bat(wo)?man")  # ? after a group means that group can appear 0 or 1 times
ba = batRegex.search("The Adventures of Batman")
# print(ba)

batRegex = re.compile(r"Bat(wo)*man")  # * after a group means that group can appear 0 or more times
ba = batRegex.search("I'm Batwowowowoman")
# print(ba)

regex = re.compile(r"(\+\*\?)+")  # + means 1 or more times
# print(regex.search("I learned about +*?+*?+*? regex syntax"))

ha = re.compile(r"(Ha){3}")  # {3} matches exactly 3 of the group
# print(ha.search("He said 'HaHaHa'"))
ha = re.compile(r"(Ha){3,5}")  # Range from 3 to 5
# print(ha.search("He said 'HaHaHaHa'"))

digit = re.compile(r"(\d){3,5}")  # Known as greedy match as it'll match the longest string possible
# print(digit.search("12345678"))

digit = re.compile(r"(\d){3,5}?")  # Non-greedy match
# print(digit.search("12345678"))
# ---------------------Character classes and findall() method---------------------
# re.search finds only the first instance
# re.findall will list all instances that match the expression
# Table 7-1 in Automate with Python
lyrics = '''12 drummers drumming,
11 pipers piping,
10 lords a-leaping,
9 ladies dancing,
8 maids a-milking,
7 swans a-swimming,
6 geese a-laying,
5 golden rings,
4 calling birds,
3 French hens,
2 turtle doves
And 1 partridge in a pear tree.'''
lyrics_regex = re.compile(r"\d+\s\w+")  # Any number of digits + space and any number of letters
# print(lyrics_regex.findall(lyrics))

vowel = re.compile(r"[aeiouAEIOU]")
# print(vowel.findall("Robocop eats baby food."))
vowel = re.compile(r"[aeiouAEIOU]{2}")  # Two vowels in a row
# print(vowel.findall("Robocop eats baby food."))
vowel = re.compile(r"[^aeiouAEIOU]")  # Caret symbol, ^, is negative expression here (do the opposite)
# print(vowel.findall("Robocop eats baby food."))
# -------------------------------.*  ^  $ character-------------------------------
begins = re.compile(r"^Hello")  # True if starts with Hello
# print(begins.search("Hello there!")
ends = re.compile(r"world!$")  # Ture if ends with world!
# print(ends.search("Hello world!")
digits = re.compile(r"^\d+$")  # Has to start and end with 1 or more digits
# print(digit.search("1234567890"))

# at = re.compile(r".at")  # . is wildcard, can match anything that has at in end of word
at = re.compile(r".{1,2}at")  # any 1 to 2 characters preceding at will be returned (including spaces)
# print(at.findall("The cat in the hat sat on the flat mat."))

name = re.compile(r"First Name: (.*) Last Name: (.*)")  # Returns anything in .* group and is greedy
# print(name.findall("First Name: Gary Last Name: Siu"))

serve = "<To serve humans> for dinner."
nongreedy = re.compile(r"<(.*?)>")  # Non-greedy .* returns minimum possible expression
# print(nongreedy.findall(serve))
serve2 = "<To serve humans> for dinner.>"
greedy = re.compile(r"<(.*)>")
# print(greedy.findall(serve2))

prime = "Serve the public trust.\nProtect the innocent.\nUpload the low."
dotStar = re.compile(r".*")  # Would only print until next new line
# print(dotStar.search(prime))
dotStar = re.compile(r".*", re.DOTALL)  # Would print everything including new line
# print(dotStar.search(prime))

vowel = re.compile(r"[aeiou]", re.I)  # I or IGNORECASE will ignore case
# print(vowel.findall("Al, why does your programming book talk about RoboCop so much?"))
# ------------------------------Sub and verbose mode------------------------------
names = re.compile(r"Agent \w+")
# print(names.findall("Agent Alice gave the secret documents to Agent Bob."))
# print(names.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob."))  # Replacing strings identified
# by REGEX
names = re.compile(r"Agent (\w)\w*")  # Returns the first letter of the REGEX
# print(names.findall("Agent Alice gave the secret documents to Agent Bob."))
# print(names.sub(r"Agent \1*****", "Agent Alice gave the secret documents to Agent Bob."))  # \1 uses the first group

number = re.compile(r"""
(\d\d\d-) |   # area code (without parens, with dash)
(\(\d\d\d\))  # -or- area code with parens and no dash
\d\d\d        # first three digits
-             # second dash
\d\d\d\d      # last 4 digits
""", re.VERBOSE)  # Makes more readable

number = re.compile(r"""
(\d\d\d-) |   # area code (without parens, with dash)
(\(\d\d\d\))  # -or- area code with parens and no dash
\d\d\d        # first three digits
-             # second dash
\d\d\d\d      # last 4 digits
""", re.VERBOSE | re.IGNORECASE | re.DOTALL)  # Can combine into compile function
