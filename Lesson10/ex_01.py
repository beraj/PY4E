fname = input('Enter a file name:')

try:
    fhand = open(fname)
except:
    print('File cannot be opened!')
    exit()

sender = dict()
sendersort = list()

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    sender[words[1]] = sender.get(words[1],0) + 1

for key, val in sender.items():
    sendersort.append((val,key))

sendersort.sort(reverse=True)

for key, val in sendersort[:1]:
    print(val, key)