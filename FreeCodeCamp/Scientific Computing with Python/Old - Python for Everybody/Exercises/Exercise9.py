
fh = open('py4e.com_code3_mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
