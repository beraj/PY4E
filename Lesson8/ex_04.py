fname = input('Enter file name:')

fhand = open(fname)

uniquewords = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word in uniquewords:
            continue
        else:
            uniquewords.append(word)

uniquewords.sort()

print(uniquewords)