fname = input('Enter a file name:')

try:
    fhand = open(fname)
except:
    print('File cannot be opened!')
    exit()

dow = dict()

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    dow[words[2]] = dow.get(words[2],0) + 1

print(dow)