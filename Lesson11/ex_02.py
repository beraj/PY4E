import re

fname = input('Enter file name:')

try:
    fhand = open(fname)
except:
    print('Could not find file!')

numlist = list()

for line in fhand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    for i in x:
        numlist.append(int(i))

revisionavg = int(sum(numlist)/len(numlist))

print(revisionavg)