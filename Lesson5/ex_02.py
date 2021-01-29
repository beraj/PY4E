#Number counter buddy!
smallest = None
largest = None

while True:
    userinput = input('Enter a number:')
    
    if userinput == 'done':
        break

    try:
        userinputint = int(userinput)
    except:
        print('Invalid input')
    
    if largest is None or userinputint > largest:
        largest = userinputint
    
    if smallest is None or userinputint < smallest:
        smallest = userinputint

print('Maximum is',largest)
print('Minimum is',smallest)