fname = input('Enter a file name:')

try:
    fhand = open(fname)
except:
    print('File cannot be opened!')
    exit()

hour = dict()
hoursort = list()

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5].split(':')
    hour[time[0]] = hour.get(time[0],0) + 1

for key, val in hour.items():
    hoursort.append((key,val))

hoursort.sort()

for key, val in hoursort:
    print(key, val)