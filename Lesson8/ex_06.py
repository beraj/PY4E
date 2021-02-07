numberlist = list()
while True:
    getnumber = input('Enter a number:')
    if getnumber == 'done':
        break
    try:
        fltnumber = float(getnumber)
    except:
        print('Please enter a number')
        continue
    numberlist.append(fltnumber)
print('Maximum:',max(numberlist))
print('Minimum:',min(numberlist))