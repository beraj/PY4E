#Grade calculator
strScore = input('Enter score: ')

try:
    fltScore = float(strScore)
except:
    print('Bad score')
    quit()

if fltScore > 1.0:
    print('Bad score')
elif fltScore >= 0.9 and fltScore <= 1.0:
    print('A')
elif fltScore >= 0.8 and fltScore <= 0.9:
    print('B')
elif fltScore >= 0.7 and fltScore <= 0.8:
    print('C')
elif fltScore >= 0.6 and fltScore <= 0.7:
    print('D')
else:
    print('F')