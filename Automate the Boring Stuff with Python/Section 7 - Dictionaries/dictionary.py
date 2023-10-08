import pprint

message = "I am some words to make up a sentence for this programme to count the letters to."

count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# pprint.pprint(count)
message_letters = pprint.pformat(count)  # Formats the dictionary for pprint and assigns that as a string
print(message_letters)
