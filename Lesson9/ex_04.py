fname = input('Enter a file name:')

try:
    fhand = open(fname)
except:
    print('File cannot be opened!')
    exit()

sender = dict()

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    sender[words[1]] = sender.get(words[1],0) + 1

largest = 0
address = ''

for key in sender:
    if sender[key] > largest:
        largest = sender[key]
        address = key
    else:
        continue

print(address,largest)