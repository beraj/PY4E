import string

fname = input('Enter a file name:')

try:
    fhand = open(fname)
except:
    print('File cannot be opened!')
    exit()

letters = dict()
letterlist = list()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = ''.join(line.lower().split())
    for x in line:
        letters[x] = letters.get(x,0) + 1

for key, val in letters.items():
    letterlist.append((key, val))

letterlist.sort()

for val, key in letterlist:
    print(key, val)
