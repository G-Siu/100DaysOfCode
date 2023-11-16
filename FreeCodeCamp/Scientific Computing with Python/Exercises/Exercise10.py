
han = open('py4e.com_code3_mbox-short.txt')

for line in han:
    line = line.rstrip()
    # print('Line:', line)
    # if line == '':
    #     # print('Skip blank')
    #     continue
    wds = line.split()
    # print('Words:', wds)
    # Guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From':
        # print('Ignore')
        continue
    print(wds[2])
