# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
add = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        pos = line.find(":")
        number = line[pos+1:]
        add += float(number.strip())
    count += 1
print("Average spam confidence:", str(add/count))
