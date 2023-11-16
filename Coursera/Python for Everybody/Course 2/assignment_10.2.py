name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        sentence = line.split()
        time = sentence[5].split(":")
        count = di.get(time[0], 0) + 1
        di[time[0]] = count
time_count = sorted(di.items())
for k, v in time_count:
    print(k, v)
