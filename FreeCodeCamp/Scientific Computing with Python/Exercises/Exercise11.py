fname = input("Enter File: ")
if len(fname) < 1: fname = 'py4e.com_code3_clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # Idiom : retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

# Find most common word
largest = -1
theword = None
for k, v in di.items():
    if v > largest:
        largest = v
        theword = k # capture/remember the word that was largest

print(theword, largest)