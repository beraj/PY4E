import re

fname = input('Enter file name:')
expinp = input('Enter a regular expression:')

try:
    fhand = open(fname)
except:
    print('Could not find file!')

count = 0

for line in fhand:
    if re.search(expinp, line):
        count = count + 1

print(f'File {fname} had {count} matching lines!')