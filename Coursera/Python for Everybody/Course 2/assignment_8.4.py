fname = input("Enter file name: ")
fh = open(fname)
lst = list()
result = list()
for line in fh:
    lst = line.split()
    for word in lst:
        if word not in result:
            result.append(word)
result.sort()
print(result)
