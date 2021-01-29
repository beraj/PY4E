def computepay(hours,rate):
    try:
        hours = float(hours)
        rate = float(rate)

        if hours > 40:
            pay = (40 * rate) + ((hours-40) * rate * 1.5)
        else:
            pay = hours * rate

        return pay
    except:
        print('Please enter a numeric value!')

h = input('Enter hours: ')
r = input('Enter rate: ')

p=computepay(h, r)

if p != None:
    print('Pay',p)