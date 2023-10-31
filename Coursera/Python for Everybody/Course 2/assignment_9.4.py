name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

words = list()
email = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:

        words = line.split()
        count = email.get(words[1], 0) + 1
        email[words[1]] = count
largest = 0
email_key = None
for k, v in email.items():
    if v > largest:
        largest = v
        email_key = k
print(email_key, largest)
