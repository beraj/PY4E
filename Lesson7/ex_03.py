#This will read all lines and print them in upper case
fname = input('Enter a file name: ')

if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()
    
try:
    fhand = open(fname)
except:
    print('File cannot be opened!')
    exit()

count = 0
total = 0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    atpos = line.find(' ')
    spamconf = line[atpos+1:]
    count = count + 1
    total = total + float(spamconf)

avgspamconf = total / count

print(f'Average spam confidence: {avgspamconf}')