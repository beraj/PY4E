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
    origaddr = words[1].split('@')
    origdomain = origaddr[1]
    sender[origdomain] = sender.get(origdomain,0) + 1

print(sender)