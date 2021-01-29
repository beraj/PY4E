#Number counter buddy!
numcount = 0
numtotal = 0

while True:
    userinput = input('Enter a number:')
    
    if userinput == 'done':
        break
    
    try:
        numtotal = numtotal + int(userinput)
    except:
        print('Invalid input')
        continue
    
    numcount = numcount + 1

numavg = numtotal / numcount

print(numtotal,numcount,numavg)