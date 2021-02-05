#This will read all lines and print them in upper case
fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened!')
    exit()

for line in fhand:
    print(line.upper().rstrip())