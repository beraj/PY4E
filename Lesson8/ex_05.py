fname = input('Enter file name:')

fhand = open(fname)

count = 0

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[1])
    count = count + 1

#Using f strings
print(f'There were {count} lines in the '
    'file with From as the first word')

#Using placeholders
print('There were %s lines in the file with from as the first word' %(count))

#Usion format method
print('There were {} lines in the file with from as the first word'.format(count))